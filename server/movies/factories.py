import asyncio
import aiohttp
import pandas as pd
import environ
import timeit
from dateutil.parser import parse

from django.db import transaction

from .models import Movie, Keyword, Staff, Credit
from .crawlers import MovieCrawler

VOTE_COUNT_LOWER_BOUND = 200

# @Params
env = environ.Env()
environ.Env.read_env()
TMDB_API_KEY = env("TMDB_API_KEY")
LANGUAGE = "ko-KR"

# @URL
TMDB_IMG_BASE_URL = "https://www.themoviedb.org/t/p/original"
YOUTUBE_BASE_URL = "https://www.youtube.com/watch?v="
TMDB_API_BASE_URL = "https://api.themoviedb.org/3"
MOVIE = "/movie"
TV = "/tv"


class MovieFactory:
    def __init__(self):
        self._csv = None
        self._api = None

    @property
    def api(self):
        self._api = self._api or self.Api()
        return self._api

    class Api:
        def __init__(self):
            self.headers = {"User-Agent": "Mozilla/5.0"}
            self.params = {"api_key": TMDB_API_KEY, "language": LANGUAGE}
            self._crawler = None

        @property
        def crawler(self):
            self._crawler = self._crawler or MovieCrawler()
            return self._crawler

        def seed(self, fetch_range: int = 100):
            loop = asyncio.get_event_loop()
            movie_details = loop.run_until_complete(self._fetch_movies(fetch_range))
            self._commit(movie_details)
            StaffFactory().api.seed(self.movie_list)

        @transaction.atomic()
        def _commit(self, movie_details):
            movies_to_create = []
            movies_to_update = []
            for movie in movie_details:
                m = Movie()
                m.title = movie.get("title")
                if not movie.get("overview"):
                    continue
                m.overview = movie.get("overview")
                m.tmdb_id = movie.get("id")
                if not movie.get("poster_path"):
                    continue
                m.poster_path = TMDB_IMG_BASE_URL + movie.get("poster_path")
                m.adult = movie.get("adult") if movie.get("adult") else False
                if (
                    not movie.get("release_date")
                    or int(movie.get("release_date")[:4]) < 1993
                ):
                    continue
                m.release_date = parse(movie.get("release_date"))
                if not movie.get("runtime"):
                    continue
                m.runtime = movie.get("runtime")

                m.video_path = movie.get("video_path")

                m._genres = []
                for genre in movie.get("genres"):
                    if genre.get("name") == "공포":
                        continue
                    m._genres.append(genre.get("name"))
                m.genre_group = ""  #

                if movie.get("vote_count") < VOTE_COUNT_LOWER_BOUND:
                    continue
                m.vote_count = movie.get("vote_count")
                if not movie.get("vote_average"):
                    continue
                m.vote_average = movie.get("vote_average") * 0.5
                if not movie.get("production_countries"):
                    continue
                m.country = movie.get("production_countries")[0].get("name")

                keywords = movie.get("keywords")
                m._keywords = keywords

                providers = movie.get("providers")
                if providers:
                    p = providers[0]
                    res = self.crawler.scrap(m.tmdb_id, p)
                    if res:
                        m._providers = [p + "::" + res] + [p for p in providers[1:]]
                    else:
                        m._providers = providers

                if Movie.objects.filter(tmdb_id=m.tmdb_id).exists():
                    movies_to_update.append(m)
                    continue
                movies_to_create.append(m)
            Movie.objects.bulk_create(movies_to_create)
            Movie.objects.bulk_update(
                movies_to_update,
                fields=["poster_path", "_genres", "_keywords"],
            )

        async def _fetch_movies(self, fetch_range: int):
            start = timeit.default_timer()

            res = []
            self.movie_list = await self._fetch_all_top_rated(fetch_range)
            movie_details = await self._fetch_all_details(self.movie_list)
            movie_videos = await self._fetch_all_videos(self.movie_list)
            movie_kwrds = await self._fetch_all_kwrds(self.movie_list)
            movie_providers = await self._fetch_all_providers(self.movie_list)

            duration = timeit.default_timer() - start
            print(f"This aiohttp requests takes {duration} second(s)")

            for i, detail in enumerate(movie_details):
                videos, kwrds, providers = (
                    movie_videos[i],
                    movie_kwrds[i],
                    movie_providers[i],
                )
                detail["video_path"] = ""
                if (
                    videos
                    and videos[0].get("site") == "YouTube"
                    and videos[0].get("key")
                ):
                    detail["video_path"] = YOUTUBE_BASE_URL + videos[0].get("key")

                detail["keywords"] = []
                if kwrds:
                    for k in kwrds:
                        detail["keywords"].append(k.get("name"))

                detail["providers"] = []
                if providers.get("KR") and providers.get("KR").get("flatrate"):
                    for p in providers.get("KR").get("flatrate"):
                        detail["providers"].append(p.get("provider_name"))

                res.append(detail)
            return res

        async def _fetch_top_rated(self, session: aiohttp.ClientSession, page: int = 1):
            async with session.get(
                TMDB_API_BASE_URL + MOVIE + "/top_rated",
                headers=self.headers,
                params=dict(self.params, **{"page": page}),
            ) as response:
                res = await response.json()
                return res.get("results")

        async def _fetch_details(self, session: aiohttp.ClientSession, movie_id: int):
            async with session.get(
                TMDB_API_BASE_URL + MOVIE + f"/{movie_id}",
                headers=self.headers,
                params=self.params,
            ) as response:
                return await response.json()

        async def _fetch_videos(self, session: aiohttp.ClientSession, movie_id: int):
            async with session.get(
                TMDB_API_BASE_URL + MOVIE + f"/{movie_id}" + "/videos",
                headers=self.headers,
                params=self.params,
            ) as response:
                res = await response.json()
                return res.get("results")

        async def _fetch_kwrds(self, session: aiohttp.ClientSession, movie_id: int):
            async with session.get(
                TMDB_API_BASE_URL + MOVIE + f"/{movie_id}" + "/keywords",
                headers=self.headers,
                params=self.params,
            ) as response:
                res = await response.json()
                return res.get("keywords")

        async def _fetch_providers(self, session: aiohttp.ClientSession, movie_id: int):
            async with session.get(
                TMDB_API_BASE_URL + MOVIE + f"/{movie_id}" + "/watch/providers",
                headers=self.headers,
                params=self.params,
            ) as response:
                res = await response.json()
                return res.get("results")

        async def _fetch_all_top_rated(self, fetch_range: int):
            async with aiohttp.ClientSession() as session:
                request_list = (
                    self._fetch_top_rated(session, page)
                    for page in range(1, fetch_range + 1)
                )
                res = []
                for page in await asyncio.gather(*request_list):
                    for movie in page:
                        res.append(movie)
                return res

        async def _fetch_all_details(self, movie_list):
            async with aiohttp.ClientSession() as session:
                request_list = (
                    self._fetch_details(session, movie.get("id"))
                    for movie in movie_list
                )
                return await asyncio.gather(*request_list)

        async def _fetch_all_videos(self, movie_list):
            async with aiohttp.ClientSession() as session:
                request_list = (
                    self._fetch_videos(session, movie.get("id")) for movie in movie_list
                )
                return await asyncio.gather(*request_list)

        async def _fetch_all_kwrds(self, movie_list):
            async with aiohttp.ClientSession() as session:
                request_list = (
                    self._fetch_kwrds(session, movie.get("id")) for movie in movie_list
                )
                return await asyncio.gather(*request_list)

        async def _fetch_all_providers(self, movie_list):
            async with aiohttp.ClientSession() as session:
                request_list = (
                    self._fetch_providers(session, movie.get("id"))
                    for movie in movie_list
                )
                return await asyncio.gather(*request_list)

    @property
    def csv(self):
        self._csv = self._csv or self.Csv()
        return self._csv

    class Csv:
        def __init__(self):
            self.data = pd.read_csv("../database/movie.csv")
            self._crawler = None

        @property
        def crawler(self):
            self._crawler = self._crawler or MovieCrawler()
            return self._crawler

        def seed(self):
            for i in range(self.data.shape[0]):
                row = self.data.iloc[i, :]
                self._commit(row)

        # protected
        def _commit(self, row):
            movie = Movie()
            movie.title = row[1]
            if row[2] == "false":
                return
            movie.overview = row[2]
            movie.tmdb_id = row[3]
            movie.poster_path = row[4]
            movie.video_path = row[5]
            movie.adult = row[6]
            if row[7] == "false":
                return
            movie.release_date = row[7]
            movie.runtime = row[8]

            genres = list(
                map(
                    lambda x: x.strip("'") if x else None,
                    row[9].replace("[", "").replace("]", "").split(", "),
                )
            )
            if "공포" in genres:
                return
            movie._genres = genres

            movie.genre_group = row[10]
            if row[11] < 200:
                return
            movie.vote_count = row[11]
            movie.vote_average = row[12]
            movie.country = row[13]

            keywords = list(
                map(
                    lambda x: x.strip("'") if x else None,
                    row[14].replace("[", "").replace("]", "").split(", "),
                )
            )
            if not keywords[0]:
                return
            movie._keywords = keywords

            movie._providers = [row[15]] if row[15] != "no" else []
            if movie._providers:
                p = movie._providers[0]
                res = self.crawler.scrap(movie.tmdb_id, p)
                if res:
                    movie._providers = [p + "::" + res]

            if Movie.objects.filter(tmdb_id=movie.tmdb_id).exists():
                return
            movie.save()
            movie = Movie.objects.get(tmdb_id=movie.tmdb_id)
            if movie.video_path == "nan":
                movie.video_path = ""
                movie.save(update_fields=["video_path"])


class StaffFactory:
    def __init__(self):
        self._csv = None
        self._api = None

    @property
    def api(self):
        self._api = self._api or self.Api()
        return self._api

    class Api:
        def __init__(self):
            self.headers = {"User-Agent": "Mozilla/5.0"}
            self.params = {"api_key": TMDB_API_KEY, "language": LANGUAGE}

        def seed(self, movie_list):
            loop = asyncio.get_event_loop()
            movie_credits = loop.run_until_complete(self._fetch_all_credits(movie_list))
            self._commit(movie_credits)

        @transaction.atomic()
        def _commit(self, movie_credits):
            staffs = []
            credits = []
            for credit in movie_credits:
                movie_tmdb_id = credit.get("id")
                if not Movie.objects.filter(tmdb_id=movie_tmdb_id).exists():
                    continue

                for i, cast in enumerate(credit.get("cast")):
                    if i > 3:
                        break

                    s = Staff()
                    if not cast.get("name"):
                        continue
                    s.name = cast.get("name")
                    s.tmdb_id = cast.get("id")
                    s.profile_path = (
                        TMDB_IMG_BASE_URL + cast.get("profile_path")
                        if cast.get("profile_path")
                        else ""
                    )
                    s.role = (
                        "Actor"
                        if cast.get("known_for_department") == "Acting"
                        else "Producer"
                    )

                    if Staff.objects.filter(tmdb_id=s.tmdb_id).exists():
                        continue
                    staffs.append(s)
                    m = Movie.objects.filter(tmdb_id=movie_tmdb_id).first()
                    if Credit.objects.filter(movie=m, staff=s).exists():
                        continue
                    c = Credit()
                    c.movie = m
                    c.staff = s
                    c.character = cast.get("character")
                    credits.append(c)
            Staff.objects.bulk_create(staffs)
            Credit.objects.bulk_create(credits)

        async def _fetch_credits(self, session: aiohttp.ClientSession, movie_id: int):
            async with session.get(
                TMDB_API_BASE_URL + MOVIE + f"/{movie_id}" + "/credits",
                headers=self.headers,
                params=self.params,
            ) as response:
                return await response.json()

        async def _fetch_all_credits(self, movie_list):
            async with aiohttp.ClientSession() as session:
                request_list = (
                    self._fetch_credits(session, movie.get("id"))
                    for movie in movie_list
                )
                return await asyncio.gather(*request_list)

    @property
    def csv(self):
        self._csv = self._csv or self.Csv()
        return self._csv

    class Csv:
        def __init__(self):
            self.data = pd.read_csv("../database/staff.csv")

        def seed(self):
            for i in range(self.data.shape[0]):
                row = self.data.iloc[i, :]
                self._commit(row)

        # protected
        def _commit(self, row):
            staff = Staff()
            if row[1] == "Unknown":
                return
            staff.name = row[1]
            staff.tmdb_id = row[2]
            if row[3][-7:] == "Unknown":
                return
            staff.profile_path = row[3]
            staff.role = row[5]

            if not Movie.objects.filter(tmdb_id=row[6]).exists():
                return
            if not Staff.objects.filter(tmdb_id=staff.tmdb_id).exists():
                staff.save()
            movie = Movie.objects.get(tmdb_id=row[6])
            staff = Staff.objects.get(tmdb_id=row[2])
            if not Credit.objects.filter(movie=movie, staff=staff).exists():
                Credit.objects.create(movie=movie, staff=staff, character=row[4])


class KeywordFactory:
    def __init__(self):
        self._csv = None
        self._api = None

    @property
    def api(self):
        self._api = self._api or self.Api()
        return self._api

    class Api:
        def __init__(self):
            self.headers = {"User-Agent": "Mozilla/5.0"}
            self.params = {"api_key": TMDB_API_KEY, "language": LANGUAGE}

        def seed(self):
            pass

    @property
    def csv(self):
        self._csv = self._csv or self.Csv()
        return self._csv

    class Csv:
        def __init__(self):
            self.data = pd.read_csv("../database/keyword.csv")

        def seed(self):
            for i in range(self.data.shape[0]):
                row = self.data.iloc[i, :]
                self._commit(row)

        # protected
        def _commit(self, row):
            keyword = Keyword()
            keyword.keyword = row[1]
            keyword.tmdb_id = row[2]
            keyword.genre_group = row[3]

            if Movie.objects.filter(keywords__contains=[keyword.keyword]).count() < 3:
                return
            if Keyword.objects.filter(tmdb_id=keyword.tmdb_id).exists():
                return
            keyword.save()

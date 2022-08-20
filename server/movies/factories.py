import asyncio
import aiohttp
import requests
import pandas as pd
import environ

from .models import Movie, Keyword, Staff, Credit
from .crawlers import MovieCrawler

# @Params
env = environ.Env()
environ.Env.read_env()
TMDB_API_KEY = env("TMDB_API_KEY")
LANGUAGE = "ko-KR"

# @URL
TMDB_IMG_BASE_URL = "https://www.themoviedb.org/t/p/original"
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

        @property
        def crawler(self):
            self._crawler = self._crawler or MovieCrawler()
            return self._crawler

        def seed(self, fetch_range: int = 100):
            loop = asyncio.get_event_loop()
            movie_details = loop.run_until_complete(self._fetch_movies(fetch_range))
            self._commit(movie_details)

        def _commit(self, movie_details):
            movies = []
            for movie in movie_details:
                m = Movie()
                m.title = movie.get("title")
                m.overview = movie.get("overview")
                m.tmdb_id = movie.get("id")
                m.poster_path = TMDB_IMG_BASE_URL + movie.get("poster_path")
                m.adult = movie.get("adult")
                if not movie.get("release_date"):
                    continue
                m.release_date = movie.get("release_date")
                m.runtime = movie.get("runtime")

                m.video_path = ""  #

                m._genres = []
                for genre in movie.get("genres"):
                    if genre.get("name") == "공포":
                        continue
                    m._genres.append(genre)
                m.genre_group = ""  #

                if movie.get("vote_count") < 200:
                    continue
                m.vote_count = movie.get("vote_count")
                m.vote_average = movie.get("vote_average") * 0.5
                if not movie.get("production_countries"):
                    continue
                m.country = movie.get("production_countries")[0].get("name")

                keywords = []  #
                m._keywords = keywords

                providers = []  #
                if providers:
                    p = providers[0]
                    res = self.crawler.scrap(m.tmdb_id, p)
                    m._providers = [p + "::" + res]

                if Movie.objects.filter(tmdb_id=m.tmdb_id).exists():
                    continue
                movies.append(m)
            Movie.objects.bulk_create(movies)

        async def _fetch_movies(self, fetch_range: int):
            movie_list = await self._fetch_all_list(fetch_range)
            return await self._fetch_all_detail(movie_list)

        async def _fetch_detail(self, session: aiohttp.ClientSession, movie_id: int):
            async with session.get(
                TMDB_API_BASE_URL + MOVIE + f"/{movie_id}",
                headers=self.headers,
                params=self.params,
            ) as response:
                return await response.json()

        async def _fetch_list(self, session: aiohttp.ClientSession, page: int = 1):
            async with session.get(
                TMDB_API_BASE_URL + MOVIE + "/top_rated",
                headers=self.headers,
                params=dict(self.params, **{"page": page}),
            ) as response:
                res = await response.json()
                return res.get("results")

        async def _fetch_all_detail(self, movie_list):
            async with aiohttp.ClientSession() as session:
                request_list = (
                    self._fetch_detail(session, movie.get("id")) for movie in movie_list
                )
                return await asyncio.gather(*request_list)

        async def _fetch_all_list(self, fetch_range: int):
            async with aiohttp.ClientSession() as session:
                request_list = (
                    self._fetch_list(session, page)
                    for page in range(1, fetch_range + 1)
                )
                res = []
                for page in await asyncio.gather(*request_list):
                    for movie in page:
                        res.append(movie)
                return res

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


class KeywordFactory:
    def __init__(self):
        self._csv = None

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


class StaffFactory:
    def __init__(self):
        self._csv = None

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
            if not Credit.objects.filter(movie=movie, staff=staff).exists:
                Credit.objects.create(movie=movie, staff=staff, character=row[4])

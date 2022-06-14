import pandas as pd

from .models import Movie, Keyword, Staff, Credit
from .crawlers import *


class MovieFactory:
    def __init__(self):
        self._csv = None

    @property
    def csv(self):
        self._csv = self._csv or self.Csv()
        return self._csv

    class Csv:
        def __init__(self):
            self.data = pd.read_csv('../database/movie.csv')
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
            if row[2] == 'false': return
            movie.overview = row[2]
            movie.tmdb_id = row[3]
            movie.poster_path = row[4]
            movie.video_path = row[5]
            movie.adult = row[6]
            if row[7] == 'false': return
            movie.release_date = row[7]
            movie.runtime = row[8]

            genres = list(map(lambda x: x.strip("'") if x else None, row[9].replace('[', '').replace(']', '').split(', ')))
            if '공포' in genres: return
            movie._genres = genres
            
            movie.genre_group = row[10]
            if row[11] < 200: return
            movie.vote_count = row[11]
            movie.vote_average = row[12]
            movie.country = row[13]

            keywords = list(map(lambda x: x.strip("'") if x else None, row[14].replace('[', '').replace(']', '').split(', ')))
            if not keywords[0]: return
            movie._keywords = keywords if keywords else []

            movie._providers = [row[15]] if row[15] != 'no' else []
            if movie._providers:
                res = self.crawler.scrap(movie.tmdb_id, movie._providers[0])
                if res: movie._providers[0] += '::' + res
            
            if Movie.objects.filter(tmdb_id=movie.tmdb_id).exists(): return
            movie.save()
            movie = Movie.objects.get(tmdb_id=movie.tmdb_id)
            if movie.video_path == 'nan':
                movie.video_path = ''
                movie.save(update_fields=['video_path'])


class KeywordFactory:
    def __init__(self):
        self._csv = None

    @property
    def csv(self):
        self._csv = self._csv or self.Csv()
        return self._csv

    class Csv:
        def __init__(self):
            self.data = pd.read_csv('../database/keyword.csv')

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

            if Movie.objects.filter(keywords__contains=[keyword.keyword]).count() < 3: return
            if Keyword.objects.filter(tmdb_id=keyword.tmdb_id).exists(): return
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
            self.data = pd.read_csv('../database/staff.csv')

        def seed(self):
            for i in range(self.data.shape[0]):
                row = self.data.iloc[i, :]
                self._commit(row)

        # protected
        def _commit(self, row):
            staff = Staff()
            if row[1] == 'Unknown': return
            staff.name = row[1]
            staff.tmdb_id = row[2]
            if row[3][-7:] == 'Unknown': return
            staff.profile_path = row[3]
            staff.role = row[5]

            if not Movie.objects.filter(tmdb_id=row[6]).exists(): return
            if not Staff.objects.filter(tmdb_id=staff.tmdb_id).exists(): staff.save()
            movie = Movie.objects.get(tmdb_id=row[6])
            staff = Staff.objects.get(tmdb_id=row[2])
            if not Credit.objects.filter(movie=movie, staff=staff).exists:
                Credit.objects.create(movie=movie, staff=staff, character=row[4])

import pandas as pd

from .models import Movie, Keyword, Staff, Credit
"""
shell_plus > from movies.factories import *
"""

def set_movies_movie(row):
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
    genre = list(map(lambda x: x.strip("'") if x else None, row[9].replace('[', '').replace(']', '').split(', ')))
    movie.genres = genre
    movie.genre_group = row[10]
    if row[11] < 200: return
    movie.vote_count = row[11]
    movie.vote_average = row[12]
    movie.country = row[13]
    keywords = list(map(lambda x: x.strip("'") if x else None, row[14].replace('[', '').replace(']', '').split(', ')))
    if not keywords[0]: return
    movie.keywords = keywords if keywords else []
    movie.providers = [row[15]] if row[15] != 'no' else []
    
    if Movie.objects.filter(tmdb_id=movie.tmdb_id).exists(): return
    movie.save()
    movie = Movie.objects.get(tmdb_id=movie.tmdb_id)
    if movie.video_path == 'nan':
        movie.video_path = ''
        movie.save(update_fields=['video_path'])


def set_movies_keyword(row):
    keyword = Keyword()
    keyword.keyword = row[1]
    keyword.tmdb_id = row[2]
    keyword.genre_group = row[3]

    if Movie.objects.filter(keywords__contains=[keyword.keyword]).count() < 3: return
    if Keyword.objects.filter(tmdb_id=keyword.tmdb_id).exists(): return
    keyword.save()


def set_movies_staff(row):
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
    Credit.objects.create(movie=movie, staff=staff, character=row[4])


data = pd.read_csv('../SetDatabase/movie.csv')
for i in range(data.shape[0]):
    row = data.iloc[i, :]
    set_movies_movie(row)

data = pd.read_csv('../SetDatabase/keyword.csv')
for i in range(data.shape[0]):
    row = data.iloc[i, :]
    set_movies_keyword(row)

data = pd.read_csv('../SetDatabase/staff.csv')
for i in range(data.shape[0]):
    row = data.iloc[i, :]
    set_movies_staff(row)

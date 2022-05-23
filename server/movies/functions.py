from .models import Movie, Keyword, Staff

def set_database(row):
    movie = Movie()
    movie.id = row[0]
    movie.title = row[1]
    movie.overview = row[2]
    movie.tmdb_id = row[3]
    movie.poster_path = row[4]
    movie.video_path = row[5]
    movie.adult = row[6]
    movie.release_date = row[7]
    movie.runtime = row[8]
    genre = row[9].replace("[", "").replace("]", "").split(', ')
    movie.genres = genre
    movie.genre_group = row[10]
    movie.vote_count = row[11]
    movie.vote_average = row[12]
    movie.country = row[13]
    keywords = row[14].replace("[", "").replace("]", "").split(', ')
    movie.keywords = keywords
    movie.providers = [row[15]]
    
    if Movie.objects.filter(tmdb_id=movie.tmdb_id).exists(): return
    movie.save()

def set_keyword_database(row):
    keywords = Keyword()
    keywords.id = row[0]
    keywords.keyword = row[1]
    keywords.tmdb_id = row[2]
    keywords.genre_group = row[3]

    if Keyword.objects.filter(tmdb_id=keywords.tmdb_id).exists(): return
    keywords.save()

def set_staff_database(row):
    staff = Staff()
    staff.id = row[0]
    staff.name = row[1]
    staff.tmdb_id = row[2]
    staff.profile_path = row[3]
    staff.character = row[4]
    staff.role = row[5]

    movie = Movie.objects.get(tmdb_id=row[6])
    staff.save()
    staff = Staff.objects.get(id=row[0])
    staff.films.add(movie)

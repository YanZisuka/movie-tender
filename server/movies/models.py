from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import ArrayField


class Movie(models.Model):

    grade_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='watch_movies', through='Grade')

    title = models.CharField(max_length=100)
    overview = models.TextField()
    poster_path = models.CharField(max_length=100)
    video_path = models.CharField(max_length=100)
    adult = models.BooleanField()
    release_date = models.IntegerField()
    runtime = models.IntegerField()
    genres = ArrayField(models.CharField(max_length=20), blank=True)
    genre_group = models.CharField(max_length=20)
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    keywords = ArrayField(models.CharField(max_length=100), blank=True)

    def has_genre(self, genre: str):
        return genre in self.genres

    def add_genre(self, genre: str):
        if self.has_genre(genre): return
        self.genres.append(genre)
        self.save(update_fields=['genres'])
        return self.genres

    def has_keyword(self, kwrd: str):
        return kwrd in self.keywords

    def add_keyword(self, kwrd: str):
        if self.has_keyword(kwrd): return
        self.keywords.append(kwrd)
        self.save(update_fields=['keywords'])
        return self.keywords

    def __str__(self):
        return f'Movie {self.pk}: {self.title}'


class Staff(models.Model):

    films = models.ManyToManyField(Movie, related_name='credits')

    name = models.CharField(max_length=100)
    profile_path = models.CharField(max_length=100)
    character = models.CharField(max_length=100)
    role = models.CharField(max_length=20)

    def __str__(self):
        return f'Staff {self.pk}: {self.name}'


class Grade(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    grade = models.FloatField()

    def __str__(self):
        return f"{self.user} gives {self.grade} for {self.movie}"


class Keyword(models.Model):

    keyword = models.CharField(max_length=100)
    genre_group = models.CharField(max_length=20)

    def __str__(self):
        return f'Keyword {self.keyword} is in {self.genre_group}'

from typing import List, Set

from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.indexes import GinIndex


class Movie(models.Model):
    class Meta:
        indexes = [
            GinIndex(fields=['_keywords']),
        ]
    """ == Schema Information
    title :`str`
    overview :`str`
    tmdb_id :`int`
    poster_path :`str`
    video_path :`str`
    adult :`bool`
    release_date :`str`
    runtime :`int`
    genres :`List[str]`
    genre_group :`str`
    vote_count :`int`
    vote_average :`float`
    country :`str`
    keywords :`List[str]`
    providers :`List[str]`
    """

    rating_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='watch_movies', through='Rating')

    title = models.CharField(max_length=100)
    overview = models.TextField()
    tmdb_id = models.IntegerField()
    poster_path = models.CharField(max_length=100)
    video_path = models.CharField(max_length=100)
    adult = models.BooleanField()
    release_date = models.CharField(max_length=30)
    runtime = models.IntegerField()
    _genres = ArrayField(models.CharField(max_length=20), blank=True, default=list, db_column='genres')
    _genre = None
    genre_group = models.CharField(max_length=20)
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    country = models.CharField(max_length=100)
    _keywords = ArrayField(models.CharField(max_length=100), blank=True, default=list, db_column='keywords')
    _keyword = None
    _providers = ArrayField(models.CharField(max_length=300), blank=True, default=list, db_column='providers')
    _provider = None

    @property
    def genres(self):
        self._genre = self._genre or self.Genres(self._genres, self)
        return self._genre

    @property
    def keywords(self):
        self._keyword = self._keyword or self.Keywords(self._keywords, self)
        return self._keyword

    @property
    def providers(self):
        self._provider = self._provider or self.Providers(self._providers, self)
        return self._provider

    class Genres:
        def __init__(self, genres: List[str], movie: 'Movie'):
            self.genres = set(genres)
            self._movie = movie

        @property
        def set(self) -> Set[str]:
            return self.genres

        def contains(self, genre: str):
            return genre in self.genres

        def add(self, genre: str):
            self.genres.add(genre)
            self._commit()

        def remove(self, genre: str):
            if not self.contains(genre): return
            self.genres.remove(genre)
            self._commit()

        def _commit(self):
            self._movie._genres = list(self.genres)
            self._movie.save(update_fields=['_genres'])

    class Keywords:
        def __init__(self, keywords: List[str], movie: 'Movie'):
            self.keywords = set(keywords)
            self._movie = movie

        @property
        def set(self) -> Set[str]:
            return self.keywords

        def contains(self, keyword: str):
            return keyword in self.keywords

        def add(self, keyword: str):
            self.keywords.add(keyword)
            self._commit()

        def remove(self, keyword: str):
            if not self.contains(keyword): return
            self.keywords.remove(keyword)
            self._commit()

        def _commit(self):
            self._movie._keywords = list(self.keywords)
            self._movie.save(update_fields=['_keywords'])

    class Providers:
        def __init__(self, providers: List[str], movie: 'Movie'):
            self.providers = set(providers)
            self._movie = movie

        @property
        def set(self) -> Set[str]:
            return self.providers

        def contains(self, provider: str):
            return provider in self.providers

        def add(self, provider: str):
            self.providers.add(provider)
            self._commit()

        def remove(self, provider: str):
            if not self.contains(provider): return
            self.providers.remove(provider)
            self._commit()

        def _commit(self):
            self._movie._providers = list(self.providers)
            self._movie.save(update_fields=['_providers'])

    def __str__(self):
        return f'Movie {self.pk}: {self.title}'


class Staff(models.Model):
    """ == Schema Information
    films :`Movie`
    name :`str`
    profile_path :`str`
    role :`str`
    """

    films = models.ManyToManyField(Movie, related_name='credits', through='Credit')

    name = models.CharField(max_length=100)
    tmdb_id = models.IntegerField()
    profile_path = models.CharField(max_length=100)
    role = models.CharField(max_length=20)

    def __str__(self):
        return f'Staff {self.pk}: {self.name}'


class Credit(models.Model):
    """ == Schema Information
    staff :`Staff`
    movie :`Movie`
    character :`str`
    """

    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    character = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.staff}'s character is {self.character} in {self.movie}"


class Rating(models.Model):
    """ == Schema Information
    user :`User`
    movie :`Movie`
    rating :`float`
    """

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    rating = models.FloatField()

    def __str__(self):
        return f"{self.user} gives {self.rating} for {self.movie}"


class Keyword(models.Model):
    """ == Schema Information
    keyword :`str`
    tmdb_id :`int`
    genre_group :`str`
    """

    keyword = models.CharField(max_length=100)
    tmdb_id = models.IntegerField()
    genre_group = models.CharField(max_length=20)

    def __str__(self):
        return f'Keyword {self.keyword} is in {self.genre_group}'

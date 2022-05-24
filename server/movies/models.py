from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import ArrayField


class Movie(models.Model):
    """title (`str`), overview (`str`), tmdb_id (`number`), poster_path (`str`), video_path (`str`), adult (`boolean`),
    release_date (`str`), runtime (`number`), genres (`List[str]`), genre_group (`str`), vote_count (`number`),
    vote_average (`number`), country (`str`), keywords (`List[str]`), providers (`List[str]`)
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
    genres = ArrayField(models.CharField(max_length=20), blank=True)
    genre_group = models.CharField(max_length=20)
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    country = models.CharField(max_length=100)
    keywords = ArrayField(models.CharField(max_length=100), blank=True)
    providers = ArrayField(models.CharField(max_length=150), blank=True, default=list)

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

    def has_provider(self, provider: str):
        return provider in self.providers

    def add_provider(self, provider: str):
        if self.has_provider(provider): return
        self.providers.append(provider)
        self.save(update_fields=['providers'])
        return self.providers

    def get_release_date(self):
        return f"{self.release_date.replace('-', '/')} (KR)"

    def get_runtime(self):
        return f'{self.runtime // 60}시간 {self.runtime % 60}분'

    def __str__(self):
        return f'Movie {self.pk}: {self.title}'


class Staff(models.Model):
    """name (`str`), profile_path: (`str`), role: (`str`), films: (class `Movie`)
    """

    films = models.ManyToManyField(Movie, related_name='credits', through='Credit')

    name = models.CharField(max_length=100)
    tmdb_id = models.IntegerField()
    profile_path = models.CharField(max_length=100)
    role = models.CharField(max_length=20)

    def __str__(self):
        return f'Staff {self.pk}: {self.name}'


class Credit(models.Model):
    """character (`str`), staff (class `Staff`), movie (class `Movie`)
    """

    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    character = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.staff}'s character is {self.character} in {self.movie}"


class Rating(models.Model):
    """rating (`number`), user (class `User`), movie (class `Movie`)
    """

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    rating = models.FloatField()

    def __str__(self):
        return f"{self.user} gives {self.rating} for {self.movie}"


class Keyword(models.Model):
    """keyword (`str`), genre_group (`str`)
    """

    keyword = models.CharField(max_length=100)
    tmdb_id = models.IntegerField()
    genre_group = models.CharField(max_length=20)

    def __str__(self):
        return f'Keyword {self.keyword} is in {self.genre_group}'

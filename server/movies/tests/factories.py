import random
from string import ascii_lowercase

import faker
from factory import Faker, LazyFunction
from factory.django import DjangoModelFactory

from movies.models import Movie, Keyword


def _random_array_fields():
    _faker = faker.Faker()
    return _faker.words(
        nb=random.randrange(1, 10), ext_word_list=ascii_lowercase, unique=True
    )


class MovieFactory(DjangoModelFactory):
    class Meta:
        model = Movie

    title = Faker("text", max_nb_chars=100)
    overview = Faker("sentence")
    tmdb_id = Faker("pyint", min_value=1)
    poster_path = "https://via.placeholder.com/800x1000.png?text=Image"
    video_path = Faker("text", max_nb_chars=100)
    adult = Faker("pybool")
    release_date = Faker("date")
    runtime = Faker("pyint", min_value=30, max_value=180)
    genre_group = Faker("text", max_nb_chars=20)
    vote_count = Faker("pyint", min_value=200)
    vote_average = Faker("pyfloat", min_value=0, max_value=5)
    country = Faker("country")
    _genres = LazyFunction(_random_array_fields)
    _keywords = LazyFunction(_random_array_fields)
    _providers = LazyFunction(_random_array_fields)


class KeywordFactory(DjangoModelFactory):
    class Meta:
        model = Keyword

    keyword = Faker("text", max_nb_chars=100)
    tmdb_id = Faker("pyint", min_value=1)
    genre_group = Faker("text", max_nb_chars=20)

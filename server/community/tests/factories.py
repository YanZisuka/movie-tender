import random
from string import ascii_lowercase

import faker
from factory import Faker, LazyFunction
from factory.django import DjangoModelFactory

from movies.models import Movie, Keyword


class ReviewFactory(DjangoModelFactory):
    pass


class CommentFactory(DjangoModelFactory):
    pass

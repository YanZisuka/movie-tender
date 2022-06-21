import random

import faker

from django.contrib.auth import get_user_model

from factory import Faker, LazyFunction
from factory.django import DjangoModelFactory


def _random_array_fields():
    _faker = faker.Faker()
    return _faker.words(nb=random.randrange(1, 10), unique=True)


class UserFactory(DjangoModelFactory):
    class Meta:
        model = get_user_model()
    
    username = Faker('pystr')
    nickname = Faker('word')
    first_name = faker.Faker('ko-KR').first_name()
    last_name = faker.Faker('ko-KR').last_name()
    email = Faker('ascii_email')
    survey = LazyFunction(_random_array_fields)
    
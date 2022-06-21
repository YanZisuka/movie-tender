from factory import Faker
from factory.django import DjangoModelFactory

from accounts.tests.factories import UserFactory
from movies.tests.factories import MovieFactory

from ..models import Review, Comment


datetime = Faker('date_time_this_decade')

class ReviewFactory(DjangoModelFactory):
    class Meta:
        model = Review

    user = UserFactory()
    movie = MovieFactory()

    content = Faker('text', max_nb_chars=100)
    created_at = datetime
    updated_at = datetime


class CommentFactory(DjangoModelFactory):
    class Meta:
        model = Comment
    
    user = UserFactory()
    review = ReviewFactory()

    content = Faker('text', max_nb_chars=100)
    created_at = datetime
    updated_at = datetime

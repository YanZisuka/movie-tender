from django.test import TestCase

from movies.models import Movie
from .factories import MovieFactory


class MovieTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.movie = MovieFactory.create(_keywords=['a', 'b'])

    def setUp(self):
        pass

    def test_키워드가_있는지_검사할수있다(self):
        assert self.movie.keywords.contains('a')
        assert not self.movie.keywords.contains('nono')

    def test_키워드를_추가할수있다(self):
        self.movie.keywords.add('word')

        assert self.movie.keywords.set == {'a', 'b', 'word'}

    def test_키워드를_삭제할수있다(self):
        self.movie.keywords.remove('a')

        assert self.movie.keywords.set == {'b'}
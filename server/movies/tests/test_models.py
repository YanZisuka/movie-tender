from django.test import TestCase

from movies.models import Movie
from .factories import MovieFactory


class MovieModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.movie = MovieFactory.create(
            _genres=["a", "b"], _keywords=["a", "b"], _providers=["a", "b"]
        )

    def test_장르가_있는지_검사할수있다(self):
        assert self.movie.genres.contains("a")
        assert not self.movie.genres.contains("nono")

    def test_장르를_추가할수있다(self):
        self.movie.genres.add("word")

        assert self.movie.genres.set == {"a", "b", "word"}

    def test_장르를_삭제할수있다(self):
        self.movie.genres.remove("a")

        assert self.movie.genres.set == {"b"}

    def test_키워드가_있는지_검사할수있다(self):
        assert self.movie.keywords.contains("a")
        assert not self.movie.keywords.contains("nono")

    def test_키워드를_추가할수있다(self):
        self.movie.keywords.add("word")

        assert self.movie.keywords.set == {"a", "b", "word"}

    def test_키워드를_삭제할수있다(self):
        self.movie.keywords.remove("a")

        assert self.movie.keywords.set == {"b"}

    def test_프로바이더가_있는지_검사할수있다(self):
        assert self.movie.providers.contains("a")
        assert not self.movie.providers.contains("nono")

    def test_프로바이더를_추가할수있다(self):
        self.movie.providers.add("word")

        assert self.movie.providers.set == {"a", "b", "word"}

    def test_프로바이더를_삭제할수있다(self):
        self.movie.providers.remove("a")

        assert self.movie.providers.set == {"b"}

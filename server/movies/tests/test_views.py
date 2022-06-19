from django.test import TestCase, Client
from django.urls import reverse

from .factories import MovieFactory, KeywordFactory


class MoviesViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        res = Client().post('/api/v1/accounts/signup/', \
            data={'username': 'credential', 'nickname': 'RandomNick', 'password1': 'qwer`123', 'password2': 'qwer`123'})
        token = res.json().get('key')
        cls.header = {'HTTP_AUTHORIZATION': f'Token {token}'}

        cls.movie = MovieFactory.create()
        cls.keyword1 = KeywordFactory.create(keyword='anime')
        cls.keyword2 = KeywordFactory.create(keyword='superhero')


    def test_영화추천을_받을수있다(self):
        res = self.client.get(reverse('movies:index'), **self.header)

        self.assertEquals(res.status_code, 200)


    def test_영화상세정보를_볼수있다(self):
        res = self.client.get(reverse('movies:movie', args=[self.movie.id]), **self.header)

        self.assertEquals(res.status_code, 200)

    def test_평점을_설정할수있다(self):
        res = self.client.post(reverse('movies:movie', args=[self.movie.id]), data={'rating': 3.5}, **self.header)

        self.assertEquals(res.status_code, 201)

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

        cls.movies = MovieFactory.create_batch(10)
        cls.keywords = []
        cls.keywords.append(KeywordFactory.create(keyword='anime'))
        cls.keywords.append(KeywordFactory.create(keyword='superhero'))


    def test_영화추천을_받을수있다(self):
        res = self.client.get(reverse('movies:index'), **self.header)

        self.assertEqual(res.status_code, 200)


    def test_영화상세정보를_볼수있다(self):
        res = self.client.get(reverse('movies:movie', args=[self.movies[0].id]), **self.header)

        self.assertEqual(res.status_code, 200)

    def test_평점을_설정할수있다(self):
        res = self.client.post(reverse('movies:movie', args=[self.movies[0].id]), data={'rating': 3.5}, **self.header)

        self.assertEqual(res.status_code, 201)


    def test_평점을_불러올수있다(self):
        res = self.client.get(reverse('movies:get_rating', args=[self.movies[0].id, 'credential']), **self.header)

        self.assertEqual(res.status_code, 200)

    
    def test_키워드에_맞는_영화를_뽑을수있다(self):
        self.movies[0].keywords.add('anime')
        self.movies[1].keywords.add('superhero')

        res = self.client.get(reverse('movies:get_movies_with_keywords', args=[2]), **self.header)

        self.assertEqual(res.status_code, 200)

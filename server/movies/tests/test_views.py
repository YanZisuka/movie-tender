import json
from string import ascii_lowercase

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from .factories import MovieFactory, KeywordFactory
from accounts.tests.factories import UserFactory

from ..models import Movie


class MoviesViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        credentials = UserFactory.build()
        credentials.password = 'qwer`123'
        
        res = Client().post('/api/v1/accounts/signup/', 
            data={
                'username': credentials.username, 
                'nickname': credentials.nickname, 
                'password1': credentials.password, 
                'password2': credentials.password,
            })
        token = res.json().get('key')
        cls.header = {'HTTP_AUTHORIZATION': f'Token {token}'}

        cls.user = get_user_model().objects.get(username=credentials.username)
        cls.movies = [MovieFactory.build_batch(100)]
        Movie.objects.bulk_create(cls.movies)
        cls.movie = MovieFactory.create(vote_average=0, vote_count=0)
        cls.keywords = [KeywordFactory.create(keyword='anime'), KeywordFactory.create(keyword='superhero')]


    def test_영화추천을_받을수있다(self):
        # survey 없는 경우
        res = self.client.get(reverse('movies:index'), **self.header)
        self.assertEqual(res.status_code, 400)
        
        # survey 있는 경우
        self.user.survey = ['anime', 'superhero'] + [a for a in ascii_lowercase]
        self.user.save(update_fields=['survey'])

        res = self.client.get(reverse('movies:index'), **self.header)
        self.assertEqual(res.status_code, 200)

    def test_서베이를_설정할수있다(self):
        data = json.dumps({
            'survey': ['anime', 'superhero']
        })
        res = self.client.put(reverse('movies:index'), data=data, content_type='application/json', **self.header)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(get_user_model().objects.get(pk=self.user.id).survey, ['anime', 'superhero'])


    def test_영화상세정보를_볼수있다(self):
        res = self.client.get(reverse('movies:movie', args=[self.movies[0].id]), **self.header)

        self.assertEqual(res.status_code, 200)

    def test_평점을_설정할수있다(self):
        res = self.client.post(reverse('movies:movie', args=[self.movie.id]), data={'rating': 3.5}, **self.header)
        self.assertEqual(res.status_code, 201)
        self.assertEqual(Movie.objects.get(pk=self.movie.id).vote_average, 3.5)
        self.assertEqual(Movie.objects.get(pk=self.movie.id).vote_count, 1)

        res = self.client.post(reverse('movies:movie', args=[self.movie.id]), data={'rating': 5}, **self.header)
        self.assertEqual(res.status_code, 201)
        self.assertEqual(Movie.objects.get(pk=self.movie.id).vote_average, 5)
        self.assertEqual(Movie.objects.get(pk=self.movie.id).vote_count, 1)


    def test_평점을_불러올수있다(self):
        res = self.client.get(reverse('movies:get_rating', args=[self.movies[0].id, self.user.username]), **self.header)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json().get('rating'), 0)

        res = self.client.post(reverse('movies:movie', args=[self.movies[0].id]), data={'rating': 4}, **self.header)
        res = self.client.get(reverse('movies:get_rating', args=[self.movies[0].id, self.user.username]), **self.header)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json().get('rating'), 4)

    
    def test_키워드에_맞는_영화를_뽑을수있다(self):
        self.movies[0].keywords.add('anime')
        self.movies[1].keywords.add('superhero')

        res = self.client.get(reverse('movies:get_movies_with_keywords', args=[2]), **self.header)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.data), 2)

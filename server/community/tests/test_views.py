import json

from django.test import TestCase, Client
from django.urls import reverse

from .factories import ReviewFactory, CommentFactory
from accounts.tests.factories import UserFactory
from movies.tests.factories import MovieFactory

from django.contrib.auth import get_user_model
from ..models import Review, Comment


class CommunityViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        credentials = UserFactory.build()
        credentials.password = 'qwer`123'
        
        res = Client().post('/api/v1/accounts/signup/', \
            data={'username': credentials.username, 'nickname': credentials.nickname, 'password1': credentials.password, 'password2': credentials.password})
        token = res.json().get('key')
        cls.header = {'HTTP_AUTHORIZATION': f'Token {token}'}

        cls.user = get_user_model().objects.get(username=credentials.username)
        cls.movie = MovieFactory.create()
        cls.reviews = [ReviewFactory.create(movie=cls.movie, user=cls.user) \
            , ReviewFactory.create(movie=cls.movie, user=cls.user)]
        cls.comment = CommentFactory.create(review=cls.reviews[1], user=cls.user)


    def test_리뷰들을_받아올수있다(self):
        res = self.client.get(reverse('community:index'), **self.header)

        self.assertEqual(res.status_code, 200)

    def test_리뷰를_작성할수있다(self):
        data = {
            'movie': self.movie.id,
            'content': 'test',
        }
        res = self.client.post(reverse('community:index'), data=data, **self.header)

        self.assertEqual(res.status_code, 201)

    
    def test_리뷰_상세정보를_볼수있다(self):
        res = self.client.get(reverse('community:review', args=[self.reviews[0].id]), **self.header)

        self.assertEqual(res.status_code, 200)

    def test_리뷰_좋아요를_할수있다(self):
        res = self.client.post(reverse('community:review', args=[self.reviews[0].id]), **self.header)

        self.assertEqual(res.status_code, 201)

    def test_리뷰_수정을_할수있다(self):
        data = json.dumps({
            'movie': self.movie.id,
            'content': 'update_test',
        })
        res = self.client.put(reverse('community:review', args=[self.reviews[0].id]), data=data, content_type='application/json', **self.header)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(Review.objects.get(pk=self.reviews[0].id).content, 'update_test')

    def test_리뷰_삭제를_할수있다(self):
        res = self.client.delete(reverse('community:review', args=[self.reviews[0].id]), **self.header)

        self.assertEqual(res.status_code, 204)

    
    def test_댓글을_작성할수있다(self):
        data = {
            'content': 'test'
        }
        res = self.client.post(reverse('community:create_comment', args=[self.reviews[1].id]), data=data, **self.header)

        self.assertEqual(res.status_code, 201)


    def test_댓글_수정을_할수있다(self):
        data = json.dumps({
            'content': 'update_test',
        })
        res = self.client.put(reverse('community:comment', args=[self.reviews[0].id, self.comment.id]), data=data, content_type='application/json', **self.header)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(Comment.objects.get(pk=self.comment.id).content, 'update_test')

    def test_댓글_삭제를_할수있다(self):
        res = self.client.delete(reverse('community:comment', args=[self.reviews[0].id, self.comment.id]), **self.header)

        self.assertEqual(res.status_code, 204)

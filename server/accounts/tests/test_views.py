import json

from django.test import TestCase, Client
from django.urls import reverse

from .factories import UserFactory

from django.contrib.auth import get_user_model


class CommunityViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        credentials = UserFactory.build()
        credentials.password = 'qwer`123'
        
        res = Client().post('/api/v1/accounts/signup/', \
            data={'username': credentials.username, 'nickname': credentials.nickname, 'password1': credentials.password, 'password2': credentials.password})
        token = res.json().get('key')
        cls.header = {'HTTP_AUTHORIZATION': f'Token {token}'}

        cls.users = [get_user_model().objects.get(username=credentials.username), UserFactory.create(password='qwer`123')]


    def test_프로필을_조회할수있다(self):
        res = self.client.get(reverse('accounts:profile', args=[self.users[0].username]), **self.header)

        self.assertEqual(res.status_code, 200)

    def test_다른유저를_팔로우할수있다(self):
        res = self.client.post(reverse('accounts:profile', args=[self.users[0].username]), **self.header)
        self.assertEqual(res.status_code, 400)

        res = self.client.post(reverse('accounts:profile', args=[self.users[1].username]), **self.header)
        self.assertEqual(res.status_code, 201)

        res = self.client.post(reverse('accounts:profile', args=[self.users[1].username]), **self.header)
        self.assertEqual(res.status_code, 204)
    
    def test_유저의_정보를_수정할수있다(self):
        data = json.dumps({
            'nickname': 'YanZisuka'
        })
        res = self.client.put(reverse('accounts:profile', args=[self.users[0].username]), data=data, content_type='application/json', **self.header)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(get_user_model().objects.get(pk=self.users[0].id).nickname, 'YanZisuka')

    def test_회원탈퇴를_할수있다(self):
        res = self.client.delete(reverse('accounts:profile', args=[self.users[0].username]), **self.header)

        self.assertEqual(res.status_code, 204)

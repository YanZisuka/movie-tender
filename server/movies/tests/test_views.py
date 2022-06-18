from django.test import TestCase, Client
from django.urls import reverse


class IndexTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        res = Client().post('/api/v1/accounts/signup/', \
            data={'username': 'credential', 'nickname': 'RandomNick', 'password1': 'qwer`123', 'password2': 'qwer`123'})
        token = res.json().get('key')
        cls.header = {'HTTP_AUTHORIZATION': f'Token {token}'}

    def test_영화추천을_받을수있다(self):
        res = self.client.get(reverse('movies:index'), **self.header)

        self.assertIs(res.status_code, 200)


class MovieTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        res = Client().post('/api/v1/accounts/signup/', \
            data={'username': 'credential', 'nickname': 'RandomNick', 'password1': 'qwer`123', 'password2': 'qwer`123'})
        token = res.json().get('key')
        cls.header = {'HTTP_AUTHORIZATION': f'Token {token}'}

    def test_영화상세정보를_볼수있다(self):
        res = self.client.get(reverse('movies:movie', args=[7]), **self.header)

        self.assertIs(res.status_code, 200)

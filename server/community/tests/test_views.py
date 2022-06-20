from django.test import TestCase, Client
from django.urls import reverse


class ReviewsViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        res = Client().post('/api/v1/accounts/signup/', \
            data={'username': 'credential', 'nickname': 'RandomNick', 'password1': 'qwer`123', 'password2': 'qwer`123'})
        token = res.json().get('key')
        cls.header = {'HTTP_AUTHORIZATION': f'Token {token}'}


    def test_리뷰들을_받아올수있다(self):
        res = self.client.get(reverse('community:index'), **self.header)

        self.assertEqual(res.status_code, 200)

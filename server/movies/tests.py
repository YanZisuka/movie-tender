from django.test import TestCase
import requests
from bs4 import BeautifulSoup as bs


SEARCH_URL = 'https://www.netflix.com/search?q=스파이패밀리'
REDIRECT_URL = 'https://www.netflix.com/kr/title/{netflix_id}'

id = '81511410'

response = requests.get(SEARCH_URL)

if response.status_code == 200:
    print(response.text)
    soup = bs(response.text, 'html.parser')
    a = soup.select_one('#title-card-0-0 > div.ptrack-content > a')
    print(a)
else:
    print(response.status_code)

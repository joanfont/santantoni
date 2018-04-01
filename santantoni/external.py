import random

from bs4 import BeautifulSoup
from cached_property import cached_property
import requests


class Cansoner:

    BASE_URL = 'http://www.fundaciocasamuseu.cat/literatura'
    LISTING_URL = 'index.php?s=canconer&ss=cercar&par=sant+antoni'

    def __init__(self):
        self._gloses = []
        self._session = requests.Session()

    @property
    def gloses(self):
        if not self._gloses:
            self._gloses = self._fetch_gloses()

        return self._gloses

    def get_random_glosa(self):
        return random.choice(self.gloses)

    def _fetch_gloses(self):
        soup = self._get_soup()
        container = soup.find('div', id='resultats_canconer')

        container_items = container.find_all('div', class_='glosa')

        return list(map(self._build_glosa, container_items))

    def _get_soup(self):
        url = f'{self.BASE_URL}/{self.LISTING_URL}'
        response = self._session.get(url)
        return BeautifulSoup(response.content, 'html.parser')

    def _build_glosa(self, item):
        brief_item = item.find('div', class_='text')
        brief = item.get_text()

        link = item.find('a')
        url = link['href']

        return Glosa(brief, url)


class Glosa:

    FULL_URL = 'http://www.fundaciocasamuseu.cat/literatura/{path}'

    def __init__(self, brief, url):
        self.brief = brief
        self.url = url



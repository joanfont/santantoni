import random

from bs4 import BeautifulSoup
import requests

class CansonerAPI:

    BASE_URL = 'http://www.fundaciocasamuseu.cat/literatura'
    LISTING_URL = 'index.php?s=canconer&ss=cercar&par=sant+antoni'

    def __init__(self):
        self._session = requests.Session()

    def fetch_gloses(self):
        url = f'{self.BASE_URL}/{self.LISTING_URL}'
        soup = self._get_soup(url)

        container = soup.find('div', id='resultats_canconer')
        container_items = container.find_all('div', class_='glosa')

        return list(map(self._build_glosa, container_items))

    def get_whole_glosa(self, glosa):
        url = f'{self.BASE_URL}/{glosa.url}'
        soup = self._get_soup(url)

        container = soup.find('div', class_='fitxa_glosa')
        whole_glosa = container.find('div', class_='text')

        return whole_glosa.get_text()

    def _build_glosa(self, item):
        brief_item = item.find('div', class_='text')
        brief = brief_item.get_text()

        link = item.find('a')
        url = link['href']

        complete_container = item.find('div', class_='completa')
        complete_link = complete_container.find('a')
        partial = complete_link is not None

        return Glosa(brief, url, partial=partial)

    def _get_soup(self, url):
        response = self._session.get(url)
        return BeautifulSoup(response.content, 'html.parser')


class Cansoner:

    def __init__(self):
        self._api = CansonerAPI()
        self._gloses = []

    @property
    def gloses(self):
        if not self._gloses:
            self._gloses = self._api.fetch_gloses()

        return self._gloses

    def get_random_glosa(self):
        gloses = self.gloses
        return random.choice(gloses)


class Glosa:

    def __init__(self, brief, url, partial=False):
        self.brief = brief
        self.url = url
        self.partial = partial

        self._whole = None
        self._api = CansonerAPI()

    @property
    def whole(self):
        if self._whole:
            return self._whole

        if not self.partial:
            self._whole = self.brief
            return self._whole

        self._whole = self._api.get_whole_glosa(self)
        return self._whole

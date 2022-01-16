import random

from bs4 import BeautifulSoup
import requests

class CansonerAPI:

    URL = 'https://www.mallorcaliteraria.cat/includes/ajax.php'
    PAYLOAD = {
        'paraulaSimple': 'sant antoni',
        'funcio': 'oralSimple'
    }


    def __init__(self):
        self._session = requests.Session()
        self._session.headers.update({
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
            'Referer': 'https://www.mallorcaliteraria.cat/ca/canconer',
            'Origin': 'https://www.mallorcaliteraria.cat',
        })

    def fetch_gloses(self):
        response = self._session.post(self.URL, data=self.PAYLOAD)
        response_payload = response.json()
        soup = BeautifulSoup(response_payload['str'], 'html.parser')

        container_items = soup.find_all('div', class_='bordGlosa')

        return list(map(self._build_glosa, container_items))

    def get_whole_glosa(self, glosa):
        body = self._session.get(glosa.url)
        soup = BeautifulSoup(body.content, 'html.parser')

        whole_glosa = soup.find('h2')

        return whole_glosa.get_text()

    def _build_glosa(self, item):
        brief_item = item.find('span')
        brief = brief_item.get_text()

        link = item.find('a')
        url = link['href']

        complete_container = item.find('small', class_='smallUnderline')
        partial = complete_container is not None

        return Glosa(brief, url, partial=partial)


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

import requests

from lugat.__version__ import __version__
from lugat.word import new as new_word

class LookupException(Exception):
    pass


URL = 'https://sozluk.gov.tr/gts?ara={}'
USER_AGENT = ('lugat/' + __version__)
REFERER = 'github.com/ademozay/lugat'
HEADERS = {
    'User-Agent': USER_AGENT,
    'Referer': REFERER,
}


def lookup(search):
    if search is None:
        return None

    try:
        response = requests.get(URL.format(search), headers=HEADERS)
        result = response.json()

        if 'error' in result:
            return None

        return new_word(result)
    except Exception as e:
        raise LookupException('lookup error') from e

import requests

try:
    from word import new as new_word
except:
    from .word import new as new_word


class LookupException(Exception):
    pass


URL = 'https://sozluk.gov.tr/gts?ara={}'
USER_AGENT = (
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/80.0.3987.87 Safari/537.36'
)
HEADERS = {
    'Host': 'sozluk.gov.tr',
    'User-Agent': USER_AGENT
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

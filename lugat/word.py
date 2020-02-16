from collections import namedtuple

Variation = namedtuple(
    'Variation', 'name origin meanings compound_words proverbs'
)
Meaning = namedtuple(
    'Meaning', 'text props samples'
)
Sample = namedtuple(
    'Sample', 'text authors'
)


class Word:
    __variations = []

    def __init__(self, words):
        for variation in words:
            self.__parse_variations(variation)

    def __parse_variations(self, variation):
        name                = variation['madde']
        origin              = variation['lisan']
        meanings            = self.__parse_meanings(variation)
        compound_words      = self.__parse_compound_words(variation)
        proverbs            = self.__parse_proverbs(variation)

        self.__variations.append(Variation(
            name, origin, meanings, compound_words, proverbs,
        ))

    def __parse_meanings(self, variation):
        meanings    = []
        _meanings   = variation.get('anlamlarListe', [])
        for m in _meanings:
            text        = m['anlam']
            props       = self.__parse_props(m)
            samples     = self.__parse_samples(m),

            if len(samples) > 0:
                samples = samples[0]

            meanings.append(Meaning(text, props, samples))

        return meanings

    def __parse_props(self, meaning):
        return list(map(
            lambda p: p['tam_adi'],
            meaning.get('ozelliklerListe', [])
        ))

    def __parse_samples(self, meaning):
        samples     = []
        _samples    = meaning.get('orneklerListe', [])

        for s in _samples:
            text    = s.get('ornek')
            authors = list(map(
                lambda a: a.get('tam_adi'),
                s.get('yazar', []),
            ))

            samples.append(Sample(text, authors))

        return samples

    def __parse_compound_words(self, variation):
        compound_words = variation.get('birlesikler', '')

        if compound_words is None: return []

        return list(map(
            lambda cw: cw.strip(),
            compound_words.split(','),
        ))

    def __parse_proverbs(self, variation):
        proverbs = variation.get('atasozu', [])

        return list(map(
            lambda p: p['madde'],
            proverbs,
        ))

    def get_variations(self):
        return self.__variations


def new(word):
    return Word(word)

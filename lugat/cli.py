import sys

from termcolor import colored

try:
    from dict import lookup, LookupException
except:
    from .dict import lookup, LookupException

HELP_TEXT = '''

    ''' + colored("TDK Güncel Türkçe Sözlük'te arama yapın.", attrs=['bold']) + '''

        ''' + colored('lugat', attrs=['bold']) + ''' mütevazı
        ''' + colored('lugat', attrs=['bold']) + ''' cefakâr

    Daha detaylı sonuçlar için:

        ''' + colored('lugat', attrs=['bold']) + ''' -v çırak
        ''' + colored('lugat', attrs=['bold']) + ''' -v usta

    * Detaylı sonuçlar; atasözleri, deyimler, birleşik fiiller ve birleşik kelimelerden oluşur.
'''

VERBOSE_FLAG = '-h'
FLAGS = [VERBOSE_FLAG]

def main():
    args = sys.argv[1:]

    if len(args) < 1:
        print(HELP_TEXT)
        exit(2)

    verbose = False
    if VERBOSE_FLAG in args:
        verbose = True
    
    remaing_args = list(filter(lambda arg: arg not in FLAGS, args))
    remaing_args = list(filter(lambda arg: not arg.startswith('-'), args))

    search = ' '.join(remaing_args)

    if not search:
        print(HELP_TEXT)
        sys.exit(2)

    word = lookup(search)

    if word is not None:
        variations = word.get_variations()

        def colorize_variations():
            text = ''
            for i, v in enumerate(variations, start=1):
                text += colored(v.name, 'yellow', attrs=['bold', 'underline'])
                if len(variations) > 2:
                    text += ' {}'.format(colored('[{}]'.format(i), attrs=['dark']))
                if v.origin:
                    text += ' - ' + colored(v.origin, 'yellow', attrs=['dark'])

                text += '\n\n'
                for m in v.meanings:
                    text += '• ' + m.text + ' '

                    if m.props:
                        text += colored(
                            ', '.join(m.props),
                            'yellow', attrs=['dark'],
                        )

                    text += '\n'
                    for s in m.samples:
                        text += '  {}  '.format(colored('Örnek', 'magenta'))
                        text += '  {}'.format(colored(s.text, 'green'))
                        if s.authors:
                            text += '\n'
                            text += '  {} '.format(colored('Yazarlar', 'magenta'))
                            text += colored(', '.join(s.authors), 'blue')
                        text += '\n'
                    else:
                        text += '\n'

                if not verbose:
                    continue

                if v.compound_words:
                    text += colored('Birleşik Kelimeler', 'cyan') + '\n'
                    text += '\n'.join(['• ' + c for c in v.compound_words])
                    text += '\n\n'

                if v.proverbs:
                    text += colored(
                        'Atasözleri, Deyimler veya Birleşik Fiiller', 'cyan'
                    )
                    text += '\n'
                    text += '\n'.join(['• ' + p for p in v.proverbs])
                    text += '\n'

            return text

        out = colorize_variations()

        print(out.rstrip('\n'))


if __name__ == "__main__":
    main()

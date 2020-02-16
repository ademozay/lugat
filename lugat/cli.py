import sys

from termcolor import colored

try:
    from dict import lookup, LookupException
except:
    from .dict import lookup, LookupException

def main():
    search = ' '.join(sys.argv[1:])
    if not search:
        print("Lütfen en az bir harf yazınız.")
        sys.exit(0)

    word = lookup(search)

    if word is not None:
        variations = word.get_variations()

        def colorize_variations():
            text = ''
            for i, v in enumerate(variations, start=1):
                text += colored(v.name, 'yellow', attrs=['bold', 'underline'])
                if len(variations) > 2:
                    text += ' {}'.format(colored(f'[{i}]', attrs=['dark']))
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
                        text += f"""  {colored('Örnek', 'magenta')}  """
                        text += f"""  {colored(s.text, 'green')}"""
                        if s.authors:
                            text += '\n'
                            text += f"""  {colored('Yazarlar', 'magenta')} """
                            text += colored(', '.join(s.authors), 'blue')
                        text += '\n'
                    else:
                        text += '\n'

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

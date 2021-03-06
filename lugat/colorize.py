
from termcolor import colored

def colorize(variations, verbose=False):
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
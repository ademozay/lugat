import json

class Alfred(dict):

    def __init__(self):
        dict.__init__(self, items=[])

    def add_item(self, item):
        self['items'].append(item)

    def alphy(self):
        return json.dumps(self, ensure_ascii=False)

class AlfredItem(dict):

    def __init__(self, title, subtitle, arg):
        dict.__init__(self,
            title=title,
            subtitle=subtitle,
            arg=arg,
            text={},
        )

    def set_clipboard_text(self, text):
        self['text']['copy'] = text

    def set_largetype_text(self, text):
        self['text']['largetype'] = text

def alphy(search, variations) -> str:
    alfred = Alfred()

    for v in variations:
        name = v.name
        for m in v.meanings:
            title       = m.text
            subtitle    = ', '.join(m.props)
            arg         = search

            if v.origin:
                subtitle = "{} - {}".format(v.origin, subtitle)

            sample = ''
            for s in m.samples:
                sample += '- {}'.format(s.text)
                if s.authors:
                    sample += '\\n'
                    sample += ', '.join(s.authors)
                break

            largetype = '{}\\n{}\\n\\n{}\\n\\n{}'.format(name, subtitle, title, sample)

            item = AlfredItem(title, subtitle, arg)

            item.set_clipboard_text(title)
            item.set_largetype_text(largetype)

            alfred.add_item(item)

    return alfred.alphy()

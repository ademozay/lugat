import sys
import unicodedata

from enum import Enum

from termcolor import colored

from lugat.__version__ import __version__

HELP_TEXT = '''

    ''' + colored("TDK Güncel Türkçe Sözlük'te arama yapın.", attrs=['bold']) + '''

        ''' + colored('lugat', attrs=['bold']) + ''' mütevazı
        ''' + colored('lugat', attrs=['bold']) + ''' cefakâr

    Daha detaylı sonuçlar için:

        ''' + colored('lugat', attrs=['bold']) + ''' -h çırak
        ''' + colored('lugat', attrs=['bold']) + ''' -h usta

    * Detaylı sonuçlar; atasözleri, deyimler, 
    birleşik fiiller ve birleşik kelimelerden oluşur.

    lugat ''' +  colored('v' + __version__, attrs=['bold'])  + '''
'''

class Args:

    class Flag(Enum):
        VERBOSE    = '-h'
        ALFRED     = '--alfred'

    flags           = [f.value for f in Flag]
    enabled_flags   = []
    input           = ''

    def __init__(self):
        args = sys.argv[1:]
        if len(args) < 1:
            sys.stdout.write(HELP_TEXT)
            exit(2)

        self._resolve_flags(args)
        self._resolve_input(args)

    def is_enabled(self, flag):
        return flag.value in self.enabled_flags

    def get_input(self):
        return self.input

    def _resolve_flags(self, args):
        for arg in args:
            for flag in self.flags:
                if flag == arg:
                    self.enabled_flags.append(flag)

    def _resolve_input(self, args):
        remaing_args    = list(filter(lambda arg: arg not in self.flags, args))
        input           = ' '.join(remaing_args)
        self.input      = self._normalize(input)

        if not self.input:
            sys.stdout.write(HELP_TEXT)
            sys.exit(2)

    def _normalize(self, text, normalization='NFC'):
        # https://www.alfredforum.com/topic/7357-encoding-in-script-filter-input/?tab=comments#comment-39232
        return unicodedata.normalize(normalization, text)
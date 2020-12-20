import sys

from lugat.__version__ import __version__

from lugat.dict import lookup
from lugat.alfred import alphy
from lugat.colorize import colorize
from lugat.args import Args

def main():
    args    = Args()
    search  = args.get_input()
    word    = lookup(search)

    if word is None:
        exit(0)

    variations = word.get_variations()

    if args.is_enabled(Args.Flag.ALFRED):
        out = alphy(search, variations)
        sys.stdout.write(out)
    else:
        verbose = args.is_enabled(Args.Flag.VERBOSE)
        out = colorize(variations, verbose)
        sys.stdout.write(out)

if __name__ == "__main__":
    main()

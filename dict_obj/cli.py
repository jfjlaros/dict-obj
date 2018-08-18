from argparse import ArgumentParser, FileType, RawDescriptionHelpFormatter

from . import doc_split, usage, version
from .dict_obj import *


def dict_obj():
    """
    """
    pass


def main():
    """Main entry point."""
    parser = ArgumentParser(
        formatter_class=RawDescriptionHelpFormatter,
        description=usage[0], epilog=usage[1])
    parser.add_argument('-v', action='version', version=version(parser.prog))

    try:
        args = parser.parse_args()
    except IOError, error:
        parser.error(error)

    try:
        dict_obj(
            **{k: v for k, v in vars(args).items()
            if k not in ('func', 'subcommand')})
    except (ValueError, IOError), error:
        parser.error(error)


if __name__ == '__main__':
    main()

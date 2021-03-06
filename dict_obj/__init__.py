from os.path import dirname, abspath

from configparser import ConfigParser

from .dict_obj import obj


config = ConfigParser()
config.readfp(open('{}/setup.cfg'.format(dirname(abspath(__file__)))))

_copyright_notice = 'Copyright (c) {} {} <{}>'.format(
    config.get('metadata', 'copyright'),
    config.get('metadata', 'author'),
    config.get('metadata', 'author_email'))


def version(name):
    return '{} version {}\n\n{}\nHomepage: {}'.format(
        config.get('metadata', 'name'),
        config.get('metadata', 'version'),
        _copyright_notice,
        config.get('metadata', 'url'))

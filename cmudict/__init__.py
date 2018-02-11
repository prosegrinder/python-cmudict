# -*- coding: utf-8 -*-

"""
This module returns the installation location of various cmudict files.
The default function where() returns the location of the cmudict.dict file.
"""

from os import path
import warnings

with open(path.join(path.dirname(__file__), 'VERSION')) as version_file:
    __version__ = version_file.read().strip()


# The directory containing the cmudict data files.
DATA_DIR = path.join(path.dirname(__file__), 'data')


def where():
    """The location of the cmudict.dict file."""
    f = path.join(DATA_DIR, 'cmudict.dict')
    return f


def where_license():
    """The location of the cmudict LICENSE file."""
    f = path.join(DATA_DIR, 'LICENSE')
    return f


def where_phones():
    """The location of the cmudict.phones file."""
    f = path.join(DATA_DIR, 'cmudict.phones')
    return f


def where_symbols():
    """The location of the cmudict.symbols file."""
    f = path.join(DATA_DIR, 'cmudict.symbols')
    return f


def where_vp():
    """The location of the cmudict.vp file."""
    f = path.join(DATA_DIR, 'cmudict.vp')
    return f


if __name__ == '__main__':
    print(where())

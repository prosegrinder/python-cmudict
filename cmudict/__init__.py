# -*- coding: utf-8 -*-

"""
This module returns the installation location of various cmudict files.
The default function where() returns the location of the cmudict.dict file.
"""

import warnings
from os import path

import pkg_resources

__version__ = pkg_resources.resource_string('cmudict', 'VERSION').strip()

def _where(filename):
    f = pkg_resources.resource_filename(__name__, filename)
    return f

def where():
    """The location of the cmudict.dict file."""
    f = pkg_resources.resource_filename(__name__, 'data/cmudict.dict')
    return f

def stream():
    """A readable file-like object of the cmudict.dict file."""
    s = pkg_resources.resource_stream(__name__, 'data/cmudict.dict')
    return s

def where_license():
    """The location of the cmudict LICENSE file."""
    f = pkg_resources.resource_filename(__name__, 'data/LICENSE')
    return f


def where_phones():
    """The location of the cmudict.phones file."""
    f = pkg_resources.resource_filename(__name__, 'data/cmudict.phones')
    return f


def where_symbols():
    """The location of the cmudict.symbols file."""
    f = pkg_resources.resource_filename(__name__, 'data/cmudict.symbols')
    return f


def where_vp():
    """The location of the cmudict.vp file."""
    f = pkg_resources.resource_filename(__name__, 'data/cmudict.vp')
    return f


if __name__ == '__main__':
    print(where())

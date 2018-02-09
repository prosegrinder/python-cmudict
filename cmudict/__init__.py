#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This module returns the installation location of various cmudict files.
The default function where() returns the location of the cmudict.dict file.
"""

from os import path
import warnings

with open(path.join(path.dirname(__file__), 'VERSION')) as version_file:
    __version__ = version_file.read().strip()


"""The directory containing the cmudict data files."""
DATA_DIR = path.join(path.dirname(__file__), 'data')


def where():
    """The location of the cmudict.dict file."""
    return path.join(DATA_DIR, 'cmudict.dict')


def where_license():
    """The location of the cmudict LICENSE file."""
    return path.join(DATA_DIR, 'LICENSE')


def where_phones():
    """The location of the cmudict.phones file."""
    return path.join(DATA_DIR, 'cmudict.phones')


def where_symbols():
    """The location of the cmudict.symbols file."""
    return path.join(DATA_DIR, 'cmudict.phones')


def where_vp():
    """The location of the cmudict.vp file."""
    return path.join(DATA_DIR, 'cmudict.vp')


if __name__ == '__main__':
    print(where())

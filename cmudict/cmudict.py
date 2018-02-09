#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
cmudict.py
~~~~~~~~~~

This module returns the installation location of various cmudict files.
The default function where() returns the location of the cmudict.dict file.
"""
import os
import warnings

"""The directory containing the cmudict data files."""
DATA_DIR = os.path.join(os.path.dirname(__file__), '/data')


def where():
    """The location of the cmudict.dict file."""
    return os.path.join(DATA_DIR, 'cmudict.dict')


def where_license():
    """The location of the cmudict LICENSE file."""
    return os.path.join(DATA_DIR, 'LICENSE')


def where_phones():
    """The location of the cmudict.phones file."""
    return os.path.join(DATA_DIR, 'cmudict.phones')


def where_symbols():
    """The location of the cmudict.symbols file."""
    return os.path.join(DATA_DIR, 'cmudict.phones')


def where_vp():
    """The location of the cmudict.vp file."""
    return os.path.join(DATA_DIR, 'cmudict.vp')


if __name__ == '__main__':
    print(where())

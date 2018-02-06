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


def data_dir():
    """The directory containing the cmudict data files."""
    return os.path.join(os.path.dirname(__file__), '/data')


def where_dict():
    """The location of the cmudict.dict file."""
    return os.path.join(data_dir(), 'cmudict.dict')


def where_phones():
    """The location of the cmudict.phones file."""
    return os.path.join(data_dir(), 'cmudict.phones')


def where_symbols():
    """The location of the cmudict.symbols file."""
    return os.path.join(data_dir(), 'cmudict.phones')


def where_vp():
    """The location of the cmudict.vp file."""
    return os.path.join(data_dir(), 'cmudict.vp')


def where_license():
    """The location of the cmudict LICENSE file."""
    return os.path.join(data_dir(), 'LICENSE')


def where():
    """The location of the cmudict.dict file."""
    return where_dict()


if __name__ == '__main__':
    print(where())

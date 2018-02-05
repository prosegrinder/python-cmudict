#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
cmudict.py
~~~~~~~~~~

This module returns the installation location of various cmudict files.
The default function where returns the location of the cmudict.dict file.
"""
import os
import warnings


def dir():
    """The directory of all the files."""
    d = os.path.dirname(__file__)

    return d


def where_dict():
    """The location of the cmudict.dict file."""
    return os.path.join(dir(), 'cmudict.dict')


def where_phonse():
    return os.path.join(dir(), 'cmudict.phones')


def where_symbols():
    return os.path.join(dir(), 'cmudict.phones')


def where_vp():
    return os.path.join(dir(), 'cmudict.vp')


def where_license():
    return os.path.join(dir(), 'LICENSE')


def where():
    """The location of the cmudict.dict file."""
    return where_dict()


if __name__ == '__main__':
    print(where())

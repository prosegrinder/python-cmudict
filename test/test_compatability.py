# -*- coding: utf-8 -*-

import cmudict


def test_dict():
    EXPECTED = 125996
    d = cmudict.dict()
    COUNT = len(d)
    if (COUNT != EXPECTED):
        raise AssertionError('cmudict.dict(): Expected {0} keys, got {1}.'.format(
            EXPECTED, COUNT))


def test_entries():
    EXPECTED = 135086
    e = cmudict.entries()
    COUNT = len(e)
    if (COUNT != EXPECTED):
        raise AssertionError('cmudict.entries(): Expected {0} entries, got {1}.'.format(
            EXPECTED, COUNT))


def test_raw():
    EXPECTED = 3615936
    r = cmudict.raw()
    COUNT = len(r)
    if (COUNT != EXPECTED):
        raise AssertionError('cmudict.raw(): Expected {0} bytes, got {1}.'.format(
            EXPECTED, COUNT))


def test_words():
    EXPECTED = 135086
    w = cmudict.words()
    COUNT = len(w)
    if (COUNT != EXPECTED):
        raise AssertionError('cmudict.raw(): Expected {0} bytes, got {1}.'.format(
            EXPECTED, COUNT))

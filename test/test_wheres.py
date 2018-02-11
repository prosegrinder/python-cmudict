# -*- coding: utf-8 -*-

import cmudict
from os import path

def _assert_filesize(filename):
    if (0 >= path.getsize(filename)):
        raise AssertionError(filename + " <= 0 bytes")

def test_where():
    _assert_filesize(cmudict.where())

def test_where_license():
    _assert_filesize(cmudict.where_license())

def test_where_phones():
    _assert_filesize(cmudict.where_phones())

def test_where_symbols():
    _assert_filesize(cmudict.where_symbols())

def test_where_vp():
    _assert_filesize(cmudict.where_vp())

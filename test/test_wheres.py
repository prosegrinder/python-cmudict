# -*- coding: utf-8 -*-

import cmudict
from os import path

def test_where():
    assert path.isfile(cmudict.where())

def test_where_license():
    assert path.isfile(cmudict.where_license())

def test_where_phones():
    assert path.isfile(cmudict.where_phones())

def test_where_symbols():
    assert path.isfile(cmudict.where_symbols())

def test_where_vp():
    assert path.isfile(cmudict.where_vp())

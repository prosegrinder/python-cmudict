# -*- coding: utf-8 -*-
from os import path

import pytest

import cmudict


class TestWheres(object):

    def __init__(self):
        self.project_dir = path.join(path.dirname(path.abspath(__file__)), '..')

    def test_where(self):
        assert cmudict.where() is self.project_dir + 'cmudict/data/cmudict.dict'

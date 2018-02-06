# -*- coding: utf-8 -*-

from .cmudict import where
from os import path

with open(path.join(path.dirname(__file__), 'VERSION')) as version_file:
    __version__ = version_file.read().strip()

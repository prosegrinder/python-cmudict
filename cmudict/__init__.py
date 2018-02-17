# -*- coding: utf-8 -*-

"""
This module provides access to the location and stream of the cmudict files.
The default function where() returns the location of the cmudict.dict file.
"""

import re
from collections import defaultdict

import pkg_resources

__version__ = pkg_resources.resource_string(
    'cmudict', 'VERSION').decode('utf-8').strip()


def _where(resource_name):
    f = pkg_resources.resource_filename(__name__, resource_name)
    return f


def _stream(resource_name):
    s = pkg_resources.resource_stream(__name__, resource_name)
    return s


def where():
    """The location of the cmudict.dict file."""
    f = _where('data/cmudict.dict')
    return f


def stream():
    """A readable file-like object of the cmudict.dict file."""
    s = _stream('data/cmudict.dict')
    return s


def where_license():
    """The location of the cmudict LICENSE file."""
    f = _where('data/LICENSE')
    return f


def stream_license():
    """A readable file-like object of the LICENSE file."""
    s = _stream('data/LICENSE')
    return s


def where_phones():
    """The location of the cmudict.phones file."""
    f = _where('data/cmudict.phones')
    return f


def stream_phones():
    """A readable file-like object of the cmudict.phones file."""
    s = _stream('data/cmudict.phones')
    return s


def where_symbols():
    """The location of the cmudict.symbols file."""
    f = _where('data/cmudict.symbols')
    return f


def stream_symbols():
    """A readable file-like object of the cmudict.symbols file."""
    s = _stream('data/cmudict.symbols')
    return s


def where_vp():
    """The location of the cmudict.vp file."""
    f = _where('data/cmudict.vp')
    return f


def stream_vp():
    """A readable file-like object of the cmudict.vp file."""
    s = _stream('data/cmudict.vp')
    return s


def dict():
    """
    Compatibility with NLTK.
    Returns the cmudict lexicon as a dictionary, whose keys are
    lowercase words and whose values are lists of pronunciations.
    """
    default = defaultdict(list)
    for key, value in entries():
        default[key].append(value)
    return default


def entries():
    """
    Compatibility with NLTK.
    Returns the cmudict lexicon as a list of entries
    containing (word, transcriptions) tuples.
    """
    entries = []
    for line in stream():
        parts = line.decode('utf-8').strip().split()
        word = re.sub(r'\(\d+\)$', '', parts[0])
        entries.append((word, parts[1:]))
    return entries


def raw():
    """
    Compatibility with NLTK.
    Returns the cmudict lexicon as a raw string.
    """
    string = pkg_resources.resource_string(__name__, 'data/cmudict.dict')
    return string.decode('utf-8')


def words():
    """
    Compatibility with NLTK.
    Returns a list of all words defined in the cmudict lexicon.
    """
    return [word.lower() for (word, _) in entries()]


if __name__ == '__main__':
    print(where())

"""cmudict

A versioned python wrapper package for The CMU Pronouncing Dictionary data
files. Compatible with NLTK's CMUDictCorpusReader.
"""

import re
import sys
from collections import defaultdict
from contextlib import ExitStack
import atexit

if sys.version_info >= (3, 9):
    from importlib import metadata, resources
else:
    import importlib_metadata as metadata
    import importlib_resources as resources

__version__ = metadata.version(__name__)

CMUDICT_DICT = "data/cmudict.dict"
CMUDICT_PHONES = "data/cmudict.phones"
CMUDICT_SYMBOLS = "data/cmudict.symbols"
CMUDICT_VP = "data/cmudict.vp"
CMUDICT_LICENSE = "data/LICENSE"

file_manager = ExitStack()
atexit.register(file_manager.close)


def _stream(resource_name):
    stream = resources.files(__name__).joinpath(resource_name).open("rb")
    return stream


def _string(resource_name):
    with resources.files(__name__).joinpath(resource_name).open() as file:
        return file.read()


def _entries(stream, comment_string=None):
    cmudict_entries = []
    for line in stream:
        parts = []
        if comment_string:
            parts = line.decode("utf-8").strip().split(comment_string)[0].split()
        else:
            parts = line.decode("utf-8").strip().split()
        thing = re.sub(r"\(\d+\)$", "", parts[0])
        cmudict_entries.append((thing, parts[1:]))
    return cmudict_entries


# pylint: disable-next=redefined-builtin
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


def dict_stream():
    """Return a readable file-like object of the cmudict.dict file."""
    stream = _stream(CMUDICT_DICT)
    return stream


def dict_string():
    """Return the contents of cmudict.dict as a string."""
    string = _string(CMUDICT_DICT)
    return string


def license_string():
    """Return the contents of LICENSE as a string."""
    string = _string(CMUDICT_LICENSE)
    return string


def phones():
    """Return a list of phones used in the main dict."""
    cmu_phones = []
    for line in phones_stream():
        parts = line.decode("utf-8").strip().split()
        cmu_phones.append((parts[0], parts[1:]))
    return cmu_phones


def phones_stream():
    """Return a readable file-like object of the cmudict.phones file."""
    p_stream = _stream(CMUDICT_PHONES)
    return p_stream


def phones_string():
    """Return the contents of cmudict.phones as a string."""
    string = _string(CMUDICT_PHONES)
    return string


def symbols():
    """Return a list of symbols."""
    cmu_symbols = []
    for line in symbols_stream():
        cmu_symbols.append(line.decode("utf-8").strip())
    return cmu_symbols


def symbols_stream():
    """Return a readable file-like object of the cmudict.symbols file."""
    stream = _stream(CMUDICT_SYMBOLS)
    return stream


def symbols_string():
    """Return the contents of cmudict.symbols as a string."""
    string = _string(CMUDICT_SYMBOLS)
    return string


# pylint: disable-next=invalid-name
def vp():
    """Return a list of punctuation pronounciations."""
    cmu_vp = defaultdict(list)
    for key, value in _entries(vp_stream()):
        cmu_vp[key].append(value)
    return cmu_vp


def vp_stream():
    """Return a readable file-like object of the cmudict.vp file."""
    stream = _stream(CMUDICT_VP)
    return stream


def vp_string():
    """Return the contents of cmudict.vp as a string."""
    string = _string(CMUDICT_VP)
    return string


# The .entries(), .raw(), and .words() functions
# maintain compatability with NTLK.
def entries():
    """
    Compatibility with NLTK.
    Returns the cmudict lexicon as a list of entries
    containing (word, transcriptions) tuples.
    """
    cmu_entries = _entries(dict_stream(), "#")
    return cmu_entries


def raw():
    """
    Compatibility with NLTK.
    Returns the cmudict lexicon as a raw string.
    """
    string = _string(CMUDICT_DICT)
    return string


def words():
    """
    Compatibility with NLTK.
    Returns a list of all words defined in the cmudict lexicon.
    """
    return [word.lower() for (word, _) in entries()]

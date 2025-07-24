"""cmudict

A versioned python wrapper package for The CMU Pronouncing Dictionary data
files. Compatible with NLTK's CMUDictCorpusReader.
"""

import atexit
import re
from contextlib import ExitStack
from importlib import metadata, resources
from typing import IO, Dict, Optional

__version__ = metadata.version(__name__)

CMUDICT_DICT = "data/cmudict.dict"
CMUDICT_PHONES = "data/cmudict.phones"
CMUDICT_SYMBOLS = "data/cmudict.symbols"
CMUDICT_VP = "data/cmudict.vp"
CMUDICT_LICENSE = "data/LICENSE"

file_manager = ExitStack()
atexit.register(file_manager.close)


def _stream(resource_name: str) -> IO[bytes]:
    stream: IO[bytes] = resources.files(__name__).joinpath(resource_name).open("rb")
    return stream


def _string(resource_name: str) -> str:
    with resources.files(__name__).joinpath(resource_name).open() as file:
        return file.read()


def _entries(
    stream: IO[bytes], comment_string: Optional[str] = None
) -> list[tuple[str, list[str]]]:
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
def dict() -> Dict[str, list[list[str]]]:
    """
    Compatibility with NLTK.
    Returns the cmudict lexicon as a dictionary, whose keys are
    lowercase words and whose values are lists of pronunciations.
    """
    default: Dict[str, list[list[str]]] = {}
    for key, value in entries():
        if key not in default:
            default[key] = []
        default[key].append(value)
    return default


def dict_stream() -> IO[bytes]:
    """Return a readable file-like object of the cmudict.dict file."""
    stream: IO[bytes] = _stream(CMUDICT_DICT)
    return stream


def dict_string() -> str:
    """Return the contents of cmudict.dict as a string."""
    string = _string(CMUDICT_DICT)
    return string


def license_string() -> str:
    """Return the contents of LICENSE as a string."""
    string = _string(CMUDICT_LICENSE)
    return string


def phones() -> list[tuple[str, list[str]]]:
    """Return a list of phones used in the main dict."""
    cmu_phones: list[tuple[str, list[str]]] = []
    for line in phones_stream():
        parts = line.decode("utf-8").strip().split()
        cmu_phones.append((parts[0], parts[1:]))
    return cmu_phones


def phones_stream() -> IO[bytes]:
    """Return a readable file-like object of the cmudict.phones file."""
    p_stream: IO[bytes] = _stream(CMUDICT_PHONES)
    return p_stream


def phones_string() -> str:
    """Return the contents of cmudict.phones as a string."""
    string = _string(CMUDICT_PHONES)
    return string


def symbols() -> list[str]:
    """Return a list of symbols."""
    cmu_symbols: list[str] = []
    for line in symbols_stream():
        cmu_symbols.append(line.decode("utf-8").strip())
    return cmu_symbols


def symbols_stream() -> IO[bytes]:
    """Return a readable file-like object of the cmudict.symbols file."""
    stream: IO[bytes] = _stream(CMUDICT_SYMBOLS)
    return stream


def symbols_string() -> str:
    """Return the contents of cmudict.symbols as a string."""
    string = _string(CMUDICT_SYMBOLS)
    return string


# pylint: disable-next=invalid-name
def vp() -> Dict[str, list[list[str]]]:
    """Return a list of punctuation pronounciations."""
    cmu_vp: Dict[str, list[list[str]]] = {}
    with vp_stream() as stream:
        for key, value in _entries(stream):
            if not key in cmu_vp:
                cmu_vp[key] = []
            cmu_vp[key].append(value)
    return cmu_vp


def vp_stream() -> IO[bytes]:
    """Return a readable file-like object of the cmudict.vp file."""
    stream: IO[bytes] = _stream(CMUDICT_VP)
    return stream


def vp_string() -> str:
    """Return the contents of cmudict.vp as a string."""
    string = _string(CMUDICT_VP)
    return string


# The .entries(), .raw(), and .words() functions
# maintain compatability with NTLK.
def entries() -> list[tuple[str, list[str]]]:
    """
    Compatibility with NLTK.
    Returns the cmudict lexicon as a list of entries
    containing (word, transcriptions) tuples.
    """
    with dict_stream() as stream:
        cmu_entries: list[tuple[str, list[str]]] = _entries(stream, "#")
    return cmu_entries


def raw() -> str:
    """
    Compatibility with NLTK.
    Returns the cmudict lexicon as a raw string.
    """
    string = _string(CMUDICT_DICT)
    return string


def words() -> list[str]:
    """
    Compatibility with NLTK.
    Returns a list of all words defined in the cmudict lexicon.
    """
    return [word.lower() for (word, _) in entries()]

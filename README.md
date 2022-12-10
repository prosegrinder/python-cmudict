# CMUdict: Python wrapper for cmudict

[![Latest PyPI version](https://img.shields.io/pypi/v/cmudict.svg)](https://pypi.python.org/pypi/cmudict)
[![GitHub Workflow Status](https://github.com/prosegrinder/python-cmudict/workflows/Python%20CI/badge.svg?branch=main)](https://github.com/prosegrinder/python-cmudict/actions?query=workflow%3A%22Python+CI%22+branch%3Amain)

CMUdict is a versioned python wrapper package for
[The CMU Pronouncing Dictionary](https://github.com/cmusphinx/cmudict) data
files. The main purpose is to expose the data with little or no assumption on
how it is to be used.

## Installation

`cmudict` is available on PyPI. Simply install it with `pip`:

```bash
pip install cmudict
```

## Usage

The cmudict data set includes 4 data files: cmudict.dict, cmudict.phones,
cmudict.symbols, and cmudict.vp. See
[The CMU Pronouncing Dictionary](https://github.com/cmusphinx/cmudict) for
details on the data. Chances are, if you're here, you already know what's in the
files.

Each file can be accessed through three functions, one which returns the raw
(string) contents, one which returns a binary stream of the file, and one which
does minimal processing of the file into an appropriate structure:

```python
>>> import cmudict

>>> cmudict.dict() # Compatible with NLTK
>>> cmudict.dict_string()
>>> cmudict.dict_stream()

>>> cmudict.phones()
>>> cmudict.phones_string()
>>> cmudict.phones_stream()

>>> cmudict.symbols()
>>> cmudict.symbols_string()
>>> cmudict.symbols_stream()

>>> cmudict.vp()
>>> cmudict.vp_string()
>>> cmudict.vp_stream()
```

Three additional functions are included to maintain compatibility with NLTK:
cmudict.entries(), cmudict.raw(), and cmudict.words(). See the
[nltk.corpus.reader.cmudict](http://www.nltk.org/_modules/nltk/corpus/reader/cmudict.html)
documentation for details:

```python
>>> cmudict.entries() # Compatible with NLTK
>>> cmudict.raw() # Compatible with NLTK
>>> cmudict.words() # Compatible with NTLK
```

And finally, the license for the cmudict data set is available as well:

```python
>>> cmudict.license_string() # Returns the cmudict license as a string
```

## Credits

Built on or modeled after the following open source projects:

- [The CMU Pronouncing Dictionary](https://github.com/cmusphinx/cmudict)
- [NLTK](https://github.com/nltk/nltk)

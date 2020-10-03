CMUdict: Python wrapper for cmudict
===================================

.. image:: https://img.shields.io/pypi/v/cmudict.svg
    :target: https://pypi.python.org/pypi/cmudict
    :alt: Latest PyPI version

.. image:: https://github.com/prosegrinder/python-cmudict/workflows/Python%20CI/badge.svg?branch=master
    :target: https://github.com/prosegrinder/python-cmudict/actions?query=workflow%3A%22Python+CI%22+branch%3Amaster
    :alt: GitHub Workflow Status

.. image:: https://app.codacy.com/project/badge/Grade/d80516541edb4dc6aa4905675b7a7ba1
    :target: https://www.codacy.com/gh/prosegrinder/python-cmudict/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=prosegrinder/python-cmudict&amp;utm_campaign=Badge_Grade
    :alt: Latest Codacy Coverage Report

`CMUdict` is a versioned python wrapper package for
`The CMU Pronouncing Dictionary`_ data files. The main purpose
is to expose the data with little or no assumption on how
it is to be used.

Installation
------------

``cmudict`` is available on PyPI. Simply install it with ``pip``::

    $ pip install cmudict

You can also install it from source::

    $ git clone https://github.com/prosegrinder/python-cmudict.git
    Cloning into 'python-cmudict'...
    ...

    $ cd python-cmudict
    $ git submodule update --init --recursive
    Submodule 'cmudict/data' (https://github.com/cmusphinx/cmudict.git) registered for path 'cmudict/data'...
    ...

    $ python setup.py install
    ...

Usage
-----

The cmudict data set includes 4 data files: cmudict.dict, cmudict.phones,
cmudict.symbols, and cmudict.vp. See `The CMU Pronouncing Dictionary`_ for
details on the data. Chances are, if you're here, you already know what's
in the files.

Each file can be accessed through three functions, one which returns the raw (string)
contents, one which returns a binary stream of the file, and one which does minimal
processing of the file into an appropriate structure::

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

Three additional functions are included to maintain compatibility with NLTK: cumdict.entries(),
cmudict.raw(), and cmudict.words(). See the `nltk.corpus.reader.cmudict`_ documentation for
details::

    >>> cmudict.entries() # Compatible with NLTK
    >>> cmudict.raw() # Compatible with NLTK
    >>> cmudict.words() # Compatible with NTLK

And finally, the license for the cmudict data set is available as well::


    >>> cmudict.license_string() # Returns the cmudict license as a string


Credits
-------

Built on or modeled after the following open source projects:

- `The CMU Pronouncing Dictionary`_
- `NLTK`_


.. _`The CMU Pronouncing Dictionary`: https://github.com/cmusphinx/cmudict
.. _`NLTK`: https://github.com/nltk/nltk
.. _`nltk.corpus.reader.cmudict`: http://www.nltk.org/_modules/nltk/corpus/reader/cmudict.html

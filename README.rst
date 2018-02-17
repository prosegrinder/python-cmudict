CMUdict: Python wrapper for cmudict
===================================

.. image:: https://travis-ci.org/prosegrinder/python-cmudict.svg?branch=master
    :target: https://travis-ci.org/prosegrinder/python-cmudict
.. image:: https://api.codacy.com/project/badge/Grade/a4cd7e19a37d4e578160d3c3e3448101
     :target: https://www.codacy.com/app/ProseGrinder/python-cmudict?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=prosegrinder/python-cmudict&amp;utm_campaign=Badge_Grade

`CMUdict` is a versioned python wrapper package for
`The CMU Pronouncing Dictionary`_ data files, and
takes a similar approach to data bundling as `Certifi`_
does with Mozilla's Root Certificates.

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

To find the location of installed cmudict data files, you can use the
built-in functions::

    >>> import cmudict

    >>> cmudict.where()
    '/usr/local/lib/python2.7/site-packages/cmudict/data/cmudict.dict'

    >>> cmudict.where_license()
    '/usr/local/lib/python2.7/site-packages/cmudict/data/LICENSE'

    >>> cmudict.where_phones()
    '/usr/local/lib/python2.7/site-packages/cmudict/data/cmudict.phones'

    >>> cmudict.where_symbols()
    '/usr/local/lib/python2.7/site-packages/cmudict/data/cmudict.symbols'

    >>> cmudict.where_vp()
    '/usr/local/lib/python2.7/site-packages/cmudict/data/cmudict.vp'

Data in the files can also be accessed directly as streams
(pkg_resources.resource_stream). Note the stream is returned
in binary mode, hence the addition of ```.decode('utf-8')```::

    >>> import cmudict

    >>> s = cmudict.stream()
    >>> for line in s:
    >>>     print(line.decode('utf-8'))
    ...

    >>> s = cmudict.stream_license()
    >>> for line in s:
    >>>     print(line.decode('utf-8'))
    ...

    >>> s = cmudict.stream_phones()
    >>> for line in s:
    >>>     print(line.decode('utf-8'))
    ...

    >>> s = cmudict.stream_symbols()
    >>> for line in s:
    >>>     print(line.decode('utf-8'))
    ...

    >>> s = cmudict.stream_vp()
    >>> for line in s:
    >>>     print(line.decode('utf-8'))
    ...

And finally, cmudict has a set of functions compatible with
`nltk.corpus.reader.cmudict`_::

    >>> import cmudict

    >>> d = cmudict.dict()
    ...

    >>> e = cmudict.entries()
    ...

    >>> r = cmudict.raw()
    ...

    >>> w = cmudict.words()
    ...

Credits
-------

Built on or modeled after the following open source projects:

- `The CMU Pronouncing Dictionary`_
- `NLTK`_
- `Certifi`_



.. _`The CMU Pronouncing Dictionary`: https://github.com/cmusphinx/cmudict
.. _`NLTK`: https://github.com/nltk/nltk
.. _`nltk.corpus.reader.cmudict`: http://www.nltk.org/_modules/nltk/corpus/reader/cmudict.html
.. _`Certifi`: https://github.com/certifi/python-certifi

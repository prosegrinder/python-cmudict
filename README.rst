CMUdict: Python wrapper for cmudict
===================================

`CMUdict` is a versioned python wrapper package for
`The CMU Pronouncing Dictionary`_ data files, and
takes a similar approach to data bundling as `Certifi`_
does for bundling Mozilla's Root Certificates.

Installation
------------

``cmudict`` is available on PyPI. Simply install it with ``pip``::

    $ pip install cmudict

Usage
-----

To reference the installed cmudict data files, you can use the
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

Credits
-------

Built on the following open source projects:

- `The CMU Pronouncing Dictionary`_
- `Certifi`_



.. _`The CMU Pronouncing Dictionary`: https://github.com/cmusphinx/cmudict
.. _`Certifi`: https://github.com/cmusphinx/cmudict

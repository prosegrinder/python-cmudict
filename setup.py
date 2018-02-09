#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup
from os import path, environ

# Version
with open(path.join(path.dirname(__file__), 'cmudict', 'VERSION'), encoding='utf-8') as version_file:
    VERSION = version_file.read().strip()
# Long Description
with open(path.join(path.dirname(__file__), 'README.rst'), encoding='utf-8') as readme_file:
    long_description = readme_file.read()


setup(
    name='cmudict',
    version=VERSION,
    description='',
    long_description=long_description,
    author='David L. Day',
    author_email='dday376@gmail.com',
    license='',
    packages=['cmudict'],
    zip_safe=False
)

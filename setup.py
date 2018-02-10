#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
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
    url='https://github.com/prosegrinder/python-cmudict',
    packages=[
        'cmudict'
    ],
    package_dir={'cmudict': 'cmudict'},
    package_data={
        '': ['LICENSE', '*.rst', 'MANIFEST.in'],
        'cmudict': [
            'VERSION',
            'data/cmudict.*',
            'data/LICENSE',
            'data/README',
            'data/README.developer'
        ]
    },
    include_package_data=True,
    zip_safe=False,
    license='GPL-3.0',
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    )
)

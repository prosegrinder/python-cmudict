#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup
from os import path

import setuptools.command.build_py

# Version
with open(path.join(path.dirname(__file__), 'VERSION'), encoding='utf-8') as version_file:
    VERSION = version_file.read().strip()
# Long Description
with open(path.join(path.dirname(__file__), 'README.rst'), encoding='utf-8') as readme_file:
    long_description = readme_file.read()

# git rev-parse HEAD
# GitPython: repo.head.commit.hexsha
# https://gitpython.readthedocs.io/en/stable/tutorial.html#the-commit-object

# git clone
# GitPython: git.Repo.clone_from
# https://gitpython.readthedocs.io/en/stable/reference.html?highlight=clone#git.repo.base.Repo.clone_from

# https://seasonofcode.com/posts/how-to-add-custom-build-steps-and-commands-to-setuppy.html
class BuildPyCommand(setuptools.command.build_py.build_py):
    """Custom build command."""

    def run(self):
        # Ref: https://stackoverflow.com/questions/15919635/on-github-api-what-is-the-best-way-to-get-the-last-commit-message-associated-w#15933109
        # 1. Get details: http https://api.github.com/repos/cmusphinx/cmudict/git/refs/heads/master
        # Use SHA-1 from response above, then:
        # 2. Get commit object: http https://api.github.com/repos/cmusphinx/cmudict/git/commits/0c74d04ece017cc205e44eb18f6305b831d74472
        # 3. Get list of objects: http https://api.github.com/repos/cmusphinx/cmudict/git/trees/0c74d04ece017cc205e44eb18f6305b831d74472?recursive=1
        # API Ref: https://developer.github.com/v3/repos/commits/

        # 1. Clean files out of ./cmudict/data
        # 2. Clone https://github.com/cmusphinx/cmudict.git to ./tmp/cmudict .
        # 3. Copy ./tmp/cmudict/* to ./cmudict/data/
        # 4. Echo SHA-1 hash from ./tmp/cmudict to ./cmudict/data/CMUDICT_SHA1
        setuptools.command.build_py.build_py.run(self)


setup(
    cmdclass={
        'build_py': BuildPyCommand
    }
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

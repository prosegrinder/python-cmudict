#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path

# Version
with open(path.join(path.dirname(__file__), 'VERSION'), encoding='utf-8') as version_file:
    VERSION = version_file.read().strip()
# Long Description
with open(path.join(path.dirname(__file__), 'README.rst'), encoding='utf-8') as readme_file:
    VERSION = readme_file.read()

# git rev-parse HEAD
# GitPython: repo.head.commit.hexsha
# https://gitpython.readthedocs.io/en/stable/tutorial.html#the-commit-object

# git clone
# GitPython: git.Repo.clone_from
# https://gitpython.readthedocs.io/en/stable/reference.html?highlight=clone#git.repo.base.Repo.clone_from

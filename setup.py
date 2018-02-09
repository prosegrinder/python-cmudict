#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from distutils.core import setup
from os import path, environ
from pathlib import Path

import requests
import setuptools.command.build_py

# Version
with open(path.join(path.dirname(__file__), 'cmudict', 'VERSION'), encoding='utf-8') as version_file:
    VERSION = version_file.read().strip()
# Long Description
with open(path.join(path.dirname(__file__), 'README.rst'), encoding='utf-8') as readme_file:
    long_description = readme_file.read()


class BuildPyCommand(setuptools.command.build_py.build_py):
    """Custom build command."""

    def run(self):

        # TODO: Validate responses
        # if response.status_code != 200:
        #     raise ApiError('Cannot call API: {}'.format(response.status_code))

        headers = {}
        # Use if available. Hit rate limit while developing. Shouldn't normally be needed.
        if environ.get('HOMEBREW_GITHUB_API_TOKEN'):
            headers['Authorization'] = 'token {0}'.format(environ.get('HOMEBREW_GITHUB_API_TOKEN'))

        # 1. Get details of master: http https://api.github.com/repos/cmusphinx/cmudict/git/refs/heads/master
        # Ref: https://stackoverflow.com/questions/15919635/on-github-api-what-is-the-best-way-to-get-the-last-commit-message-associated-w#15933109
        # cmudict_master = json.loads(requests.get(
        #     'https://api.github.com/repos/cmusphinx/cmudict/git/refs/heads/master').text)
        cmudict_master = json.loads(requests.get(
            'https://api.github.com/repos/izuzak/pmrpc/git/refs/heads/master', headers=headers).text)
        cmducit_sha1 = cmudict_master['object']['sha']
        # Use SHA-1 from response above, then:
        # 2. Get commit object recursively: http https://api.github.com/repos/cmusphinx/cmudict/git/commits/0c74d04ece017cc205e44eb18f6305b831d74472
        latest_commit = json.loads(requests.get(cmudict_master['object']['url'], headers=headers).text)
        # 3. Get list of objects: http https://api.github.com/repos/cmusphinx/cmudict/git/trees/9d0d34471e929f4eefb764542a1ec0073fda61e2?recursive=1
        # API Ref: https://developer.github.com/v3/repos/commits/
        payload = {'recursive': 1}
        commit_tree = json.loads(requests.get(latest_commit['tree']['url'], params=payload, headers=headers).text)
        for obj in commit_tree['tree']:
            if obj['type'] == 'tree':
                local_dir = Path(path.join(path.dirname(__file__), 'cmudict', 'data', obj['path']))
                print(local_dir)
                local_dir.mkdir(parents=True, exist_ok=True)
            elif obj['type'] == 'blob':
                print(path.abspath(path.join(path.dirname(__file__), 'cmudict', 'data', obj['path'])))
            else:
                pass

        # 1. Clean files out of ./cmudict/data
        # 2. Clone https://github.com/cmusphinx/cmudict.git to ./tmp/cmudict .
        # 3. Copy ./tmp/cmudict/* to ./cmudict/data/
        # 4. Echo SHA-1 hash from ./tmp/cmudict to ./cmudict/data/CMUDICT_SHA1
        setuptools.command.build_py.build_py.run(self)


setup(
    cmdclass={
        'build_py': BuildPyCommand
    },
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

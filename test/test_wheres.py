# -*- coding: utf-8 -*-

import pkg_resources

import cmudict


def test_where():
    filename = cmudict.where()
    expected_filename = pkg_resources.resource_filename(
        'cmudict', 'data/cmudict.dict')
    if (filename != expected_filename):
        raise AssertionError('cmudict.dict: Expected {0}, got {1}.'.format(
            filename, expected_filename))


def test_where_license():
    filename = cmudict.where_license()
    expected_filename = pkg_resources.resource_filename(
        'cmudict', 'data/LICENSE')
    if (filename != expected_filename):
        raise AssertionError('LICENSE: Expected {0}, got {1}.'.format(
            filename, expected_filename))


def test_where_phones():
    filename = cmudict.where_phones()
    expected_filename = pkg_resources.resource_filename(
        'cmudict', 'data/cmudict.phones')
    if (filename != expected_filename):
        raise AssertionError('cmudict.phones: Expected {0}, got {1}.'.format(
            filename, expected_filename))


def test_where_symbols():
    filename = cmudict.where_symbols()
    expected_filename = pkg_resources.resource_filename(
        'cmudict', 'data/cmudict.symbols')
    if (filename != expected_filename):
        raise AssertionError('cmudict.symbols: Expected {0}, got {1}.'.format(
            filename, expected_filename))


def test_where_vp():
    filename = cmudict.where_vp()
    expected_filename = pkg_resources.resource_filename(
        'cmudict', 'data/cmudict.vp')
    if (filename != expected_filename):
        raise AssertionError('cmudict.vp: Expected {0}, got {1}.'.format(
            filename, expected_filename))

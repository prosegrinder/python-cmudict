# -*- coding: utf-8 -*-

import pkg_resources

import cmudict


def test_stream():
    stream = cmudict.stream()
    expected_stream = pkg_resources.resource_stream(
        'cmudict', 'data/cmudict.dict')
    if (stream.name != expected_stream.name):
        raise AssertionError('cmudict.dict: Expected {0}, got {1}.'.format(
            stream.name, expected_stream.name))


def test_stream_license():
    stream = cmudict.stream_license()
    expected_stream = pkg_resources.resource_stream(
        'cmudict', 'data/LICENSE')
    if (stream.name != expected_stream.name):
        raise AssertionError('LICENSE: Expected {0}, got {1}.'.format(
            stream.name, expected_stream.name))


def test_stream_phones():
    stream = cmudict.stream_phones()
    expected_stream = pkg_resources.resource_stream(
        'cmudict', 'data/cmudict.phones')
    if (stream.name != expected_stream.name):
        raise AssertionError('cmudict.phones: Expected {0}, got {1}.'.format(
            stream.name, expected_stream.name))


def test_stream_symbols():
    stream = cmudict.stream_symbols()
    expected_stream = pkg_resources.resource_stream(
        'cmudict', 'data/cmudict.symbols')
    if (stream.name != expected_stream.name):
        raise AssertionError('cmudict.symbols: Expected {0}, got {1}.'.format(
            stream.name, expected_stream.name))


def test_stream_vp():
    stream = cmudict.stream_vp()
    expected_stream = pkg_resources.resource_stream(
        'cmudict', 'data/cmudict.vp')
    if (stream.name != expected_stream.name):
        raise AssertionError('cmudict.vp: Expected {0}, got {1}.'.format(
            stream.name, expected_stream.name))

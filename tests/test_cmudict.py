# -*- coding: utf-8 -*-

import cmudict


def test_dict_string():
    EXPECTED_LENGTH = 3616055
    dict_string = cmudict.dict_string()
    LENGTH = len(dict_string)
    if (EXPECTED_LENGTH != LENGTH):
        raise AssertionError('cmudict.dict_string(): Expected {0} length, got {1}.'.format(
            EXPECTED_LENGTH, LENGTH))


def test_dict_comments():
    DICT = cmudict.dict()
    TEST_DICT = {
        "d'artagnan": [['D', 'AH0', 'R', 'T', 'AE1', 'NG', 'Y', 'AH0', 'N']],
        "danglar": [['D', 'AH0', 'NG', 'L', 'AA1', 'R']],
        "danglars": [['D', 'AH0', 'NG', 'L', 'AA1', 'R', 'Z']],
        "gdp": [['G', 'IY1', 'D', 'IY1', 'P', 'IY1']],
        "hiv": [['EY1', 'CH', 'AY1', 'V', 'IY1']],
        "porthos": [['P', 'AO0', 'R', 'T', 'AO1', 'S']],
        "spieth": [['S', 'P', 'IY1', 'TH'], ['S', 'P', 'AY1', 'AH0', 'TH']]
    }
    for TEST_WORD in TEST_DICT:
        EXPECTED_PRONOUNCIATION = TEST_DICT[TEST_WORD]
        PRONUNCIATION = DICT[TEST_WORD]
        if EXPECTED_PRONOUNCIATION != PRONUNCIATION:
            raise AssertionError('cmudict.dict(): Expected "{0}", got "{1}".'.format(
                EXPECTED_PRONOUNCIATION, PRONUNCIATION))


def test_phones():
    EXPECTED_SIZE = 39
    phones = cmudict.phones()
    SIZE = len(phones)
    if (EXPECTED_SIZE != SIZE):
        raise AssertionError('cmudict.phones(): Expected {0} keys, got {1}.'.format(
            EXPECTED_SIZE, SIZE))


def test_phones_string():
    EXPECTED_LENGTH = 382
    phones_string = cmudict.phones_string()
    LENGTH = len(phones_string)
    if (EXPECTED_LENGTH != LENGTH):
        raise AssertionError('cmudict.phones_string(): Expected {0} length, got {1}.'.format(
            EXPECTED_LENGTH, LENGTH))


def test_symbols():
    EXPECTED_SIZE = 84
    symbols = cmudict.symbols()
    SIZE = len(symbols)
    if (EXPECTED_SIZE != SIZE):
        raise AssertionError('cmudict.symbols(): Expected {0} keys, got {1}.'.format(
            EXPECTED_SIZE, SIZE))


def test_symbols_string():
    EXPECTED_LENGTH = 281
    symbols_string = cmudict.symbols_string()
    LENGTH = len(symbols_string)
    if (EXPECTED_LENGTH != LENGTH):
        raise AssertionError('cmudict.symbols_string(): Expected {0} length, got {1}.'.format(
            EXPECTED_LENGTH, LENGTH))


def test_vp():
    EXPECTED_SIZE = 52
    vp = cmudict.vp()
    SIZE = len(vp)
    if (EXPECTED_SIZE != SIZE):
        raise AssertionError('cmudict.vp(): Expected {0} keys, got {1}.'.format(
            EXPECTED_SIZE, SIZE))


def test_vp_string():
    EXPECTED_LENGTH = 1747
    vp_string = cmudict.vp_string()
    LENGTH = len(vp_string)
    if (EXPECTED_LENGTH != LENGTH):
        raise AssertionError('cmudict.vp_string(): Expected {0} length, got {1}.'.format(
            EXPECTED_LENGTH, LENGTH))


def test_license_string():
    EXPECTED_LENGTH = 1754
    license_string = cmudict.license_string()
    LENGTH = len(license_string)
    if (EXPECTED_LENGTH != LENGTH):
        raise AssertionError('cmudict.license_string(): Expected {0} length, got {1}.'.format(
            EXPECTED_LENGTH, LENGTH))

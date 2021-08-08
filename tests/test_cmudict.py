# -*- coding: utf-8 -*-

import cmudict


def test_dict_string():
    EXPECTED_LENGTH = 3618090
    dict_string = cmudict.dict_string()
    LENGTH = len(dict_string)
    if (EXPECTED_LENGTH != LENGTH):
        raise AssertionError('cmudict.dict_string(): Expected {0} length, got {1}.'.format(
            EXPECTED_LENGTH, LENGTH))


def test_dict_comments():
    DICT = cmudict.dict()
    EXPECTED_DICT = {
        "d'artagnan": [['D', 'AH0', 'R', 'T', 'AE1', 'NG', 'Y', 'AH0', 'N']],
        "danglar": [['D', 'AH0', 'NG', 'L', 'AA1', 'R']],
        "danglars": [['D', 'AH0', 'NG', 'L', 'AA1', 'R', 'Z']],
        "gdp": [['G', 'IY1', 'D', 'IY1', 'P', 'IY1']],
        "hiv": [['EY1', 'CH', 'AY1', 'V', 'IY1']],
        "porthos": [['P', 'AO0', 'R', 'T', 'AO1', 'S']],
        "spieth": [['S', 'P', 'IY1', 'TH'], ['S', 'P', 'AY1', 'AH0', 'TH']]
    }
    for TEST_WORD in EXPECTED_DICT:
        EXPECTED_PRONOUNCIATION = EXPECTED_DICT[TEST_WORD]
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


def test_vp_comments():
    VP = cmudict.vp()
    EXPECTED_VP = {
        '!exclamation-point': [['EH2', 'K', 'S', 'K', 'L', 'AH0', 'M', 'EY1', 'SH', 'AH0', 'N', 'P', 'OY2', 'N', 'T']],
        '"close-quote': [['K', 'L', 'OW1', 'Z', 'K', 'W', 'OW1', 'T']],
        '"double-quote': [['D', 'AH1', 'B', 'AH0', 'L', 'K', 'W', 'OW1', 'T']],
        '"end-of-quote': [['EH1', 'N', 'D', 'AH0', 'V', 'K', 'W', 'OW1', 'T']],
        '"end-quote': [['EH1', 'N', 'D', 'K', 'W', 'OW1', 'T']],
        '"in-quotes': [['IH1', 'N', 'K', 'W', 'OW1', 'T', 'S']],
        '"quote': [['K', 'W', 'OW1', 'T']],
        '"unquote': [['AH1', 'N', 'K', 'W', 'OW1', 'T']],
        '#sharp-sign': [['SH', 'AA1', 'R', 'P', 'S', 'AY1', 'N']],
        '%percent': [['P', 'ER0', 'S', 'EH1', 'N', 'T']],
        '&ampersand': [['AE1', 'M', 'P', 'ER0', 'S', 'AE2', 'N', 'D']],
        '(begin-parens': [['B', 'IH0', 'G', 'IH1', 'N', 'P', 'ER0', 'EH1', 'N', 'Z']],
        '(in-parentheses': [['IH1', 'N', 'P', 'ER0', 'EH1', 'N', 'TH', 'AH0', 'S', 'IY2', 'Z']],
        '(left-paren': [['L', 'EH1', 'F', 'T', 'P', 'ER0', 'EH1', 'N']],
        '(open-parentheses': [['OW1', 'P', 'AH0', 'N', 'P', 'ER0', 'EH1', 'N', 'TH', 'AH0', 'S', 'IY2', 'Z']],
        '(paren': [['P', 'ER0', 'EH1', 'N']], '(parens': [['P', 'ER0', 'EH1', 'N', 'Z']],
        '(parentheses': [['P', 'ER0', 'EH1', 'N', 'TH', 'AH0', 'S', 'IY2', 'Z']],
        ')close-paren': [['K', 'L', 'OW1', 'Z', 'P', 'ER0', 'EH1', 'N']],
        ')close-parentheses': [['K', 'L', 'OW1', 'Z', 'P', 'ER0', 'EH1', 'N', 'TH', 'AH0', 'S', 'IY2', 'Z']],
        ')end-paren': [['EH1', 'N', 'D', 'P', 'ER0', 'EH1', 'N']],
        ')end-parens': [['EH1', 'N', 'D', 'P', 'ER0', 'EH1', 'N', 'Z']],
        ')end-parentheses': [['EH1', 'N', 'D', 'P', 'ER0', 'EH1', 'N', 'TH', 'AH0', 'S', 'IY2', 'Z']],
        ')end-the-paren': [['EH1', 'N', 'D', 'DH', 'AH0', 'P', 'ER0', 'EH1', 'N']],
        ')paren': [['P', 'ER0', 'EH1', 'N']],
        ')parens': [['P', 'ER0', 'EH1', 'N', 'Z']],
        ')right-paren': [['R', 'AY1', 'T', 'P', 'ER0', 'EH1', 'N'], ['R', 'AY1', 'T', 'P', 'EH1', 'R', 'AH0', 'N']],
        ')un-parentheses': [['AH1', 'N', 'P', 'ER0', 'EH1', 'N', 'TH', 'AH0', 'S', 'IY1', 'Z']],
        ',comma': [['K', 'AA1', 'M', 'AH0']], '-dash': [['D', 'AE1', 'SH']],
        '-hyphen': [['HH', 'AY1', 'F', 'AH0', 'N']],
        '...ellipsis': [['IH0', 'L', 'IH1', 'P', 'S', 'IH0', 'S']],
        '.decimal': [['D', 'EH1', 'S', 'AH0', 'M', 'AH0', 'L']],
        '.dot': [['D', 'AA1', 'T']],
        '.full-stop': [['F', 'UH1', 'L', 'S', 'T', 'AA1', 'P']],
        '.period': [['P', 'IH1', 'R', 'IY0', 'AH0', 'D']],
        '.point': [['P', 'OY1', 'N', 'T']],
        '/slash': [['S', 'L', 'AE1', 'SH']],
        ':colon': [['K', 'OW1', 'L', 'AH0', 'N']],
        ';semi-colon': [['S', 'EH1', 'M', 'IY0', 'K', 'OW1', 'L', 'AH0', 'N'], ['S', 'EH1', 'M', 'IH0', 'K', 'OW2', 'L', 'AH0', 'N']],
        '?question-mark': [['K', 'W', 'EH1', 'S', 'CH', 'AH0', 'N', 'M', 'AA1', 'R', 'K']],
        '{brace': [['B', 'R', 'EY1', 'S']], '{left-brace': [['L', 'EH1', 'F', 'T', 'B', 'R', 'EY1', 'S']],
        '{open-brace': [['OW1', 'P', 'EH0', 'N', 'B', 'R', 'EY1', 'S']],
        '}close-brace': [['K', 'L', 'OW1', 'Z', 'B', 'R', 'EY1', 'S']],
        '}right-brace': [['R', 'AY1', 'T', 'B', 'R', 'EY1', 'S']],
        "'end-inner-quote": [['EH1', 'N', 'D', 'IH1', 'N', 'ER0', 'K', 'W', 'OW1', 'T']],
        "'end-quote": [['EH1', 'N', 'D', 'K', 'W', 'OW1', 'T']],
        "'inner-quote": [['IH1', 'N', 'ER0', 'K', 'W', 'OW1', 'T']],
        "'single-quote": [['S', 'IH1', 'NG', 'G', 'AH0', 'L', 'K', 'W', 'OW1', 'T']],
        "'quote": [['K', 'W', 'OW1', 'T']],
        "'apostrophe": [['AH0', 'P', 'AA1', 'S', 'T', 'R', 'AH0', 'F', 'IY0']]
    }
    for PUNCTUATION in EXPECTED_VP:
        EXPECTED_PRONOUNCIATION = EXPECTED_VP[PUNCTUATION]
        PRONUNCIATION = VP[PUNCTUATION]
        if EXPECTED_PRONOUNCIATION != PRONUNCIATION:
            raise AssertionError('cmudict.vp(): Expected "{0}", got "{1}".'.format(
                EXPECTED_PRONOUNCIATION, PRONUNCIATION))


def test_license_string():
    EXPECTED_LENGTH = 1754
    license_string = cmudict.license_string()
    LENGTH = len(license_string)
    if (EXPECTED_LENGTH != LENGTH):
        raise AssertionError('cmudict.license_string(): Expected {0} length, got {1}.'.format(
            EXPECTED_LENGTH, LENGTH))

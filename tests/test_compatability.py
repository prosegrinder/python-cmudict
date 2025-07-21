# pylint: disable=missing-docstring
import cmudict


def test_dict():
    expected_size = 126052
    d = cmudict.dict()
    actual_size = len(d)
    if expected_size != actual_size:
        raise AssertionError(
            f"cmudict.dict(): Expected {expected_size} keys, got {actual_size}."
        )


def test_entries():
    expected_count = 135166
    e = cmudict.entries()
    actual_count = len(e)
    if actual_count != expected_count:
        raise AssertionError(
            f"cmudict.entries(): Expected {expected_count} entries, got {actual_count}."
        )


def test_raw():
    expected_bytes = 3618488
    r = cmudict.raw()
    actual_bytes = len(r)
    if actual_bytes != expected_bytes:
        raise AssertionError(
            f"cmudict.raw(): Expected {expected_bytes} bytes, got {actual_bytes}."
        )


def test_words():
    expected_count = 135166
    w = cmudict.words()
    actual_count = len(w)
    if actual_count != expected_count:
        raise AssertionError(
            f"cmudict.words(): Expected {expected_count} words, got {actual_count}."
        )

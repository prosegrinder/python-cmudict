# pylint: disable=missing-docstring
import cmudict


def test_dict_stream():
    expected_length = 135166
    # borrowed from pronouncingpy to ensure compatibility
    pronunciations = list()
    filehandle = cmudict.dict_stream()
    for line in filehandle:
        line = line.strip().decode("utf-8")
        if line.startswith(";"):
            continue
        word, phones = line.split(" ", 1)
        pronunciations.append((word.split("(", 1)[0].lower(), phones))
    filehandle.close()
    assert len(pronunciations) == expected_length


def test_dict_string():
    expected_length = 3618488
    dict_string = cmudict.dict_string()
    actual_length = len(dict_string)
    if expected_length != actual_length:
        raise AssertionError(
            f"cmudict.dict_string(): Expected {expected_length} length, got {actual_length}."
        )


def test_dict_comments():
    actual_dict = cmudict.dict()
    expected_dict = {
        "d'artagnan": [["D", "AH0", "R", "T", "AE1", "NG", "Y", "AH0", "N"]],
        "danglar": [["D", "AH0", "NG", "L", "AA1", "R"]],
        "danglars": [["D", "AH0", "NG", "L", "AA1", "R", "Z"]],
        "gdp": [["G", "IY1", "D", "IY1", "P", "IY1"]],
        "hiv": [["EY1", "CH", "AY1", "V", "IY1"]],
        "porthos": [["P", "AO0", "R", "T", "AO1", "S"]],
        "spieth": [["S", "P", "IY1", "TH"], ["S", "P", "AY1", "AH0", "TH"]],
    }
    for test_word, expected_pronunciation in expected_dict.items():
        actual_pronunciation = actual_dict[test_word]
        if expected_pronunciation != actual_pronunciation:
            raise AssertionError(
                f"""
                cmudict.dict(): Expected "{expected_pronunciation}", got "{actual_pronunciation}".
                """
            )


def test_phones():
    expected_size = 39
    phones = cmudict.phones()
    actual_size = len(phones)
    if expected_size != actual_size:
        raise AssertionError(
            f"cmudict.phones(): Expected {expected_size} keys, got {actual_size}."
        )


def test_phones_string():
    expected_length = 382
    phones_string = cmudict.phones_string()
    actual_length = len(phones_string)
    if expected_length != actual_length:
        raise AssertionError(
            f"cmudict.phones_string(): Expected {expected_length} length, got {actual_length}."
        )


def test_symbols():
    expected_size = 84
    symbols = cmudict.symbols()
    actual_size = len(symbols)
    if expected_size != actual_size:
        raise AssertionError(
            f"cmudict.symbols(): Expected {expected_size} keys, got {actual_size}."
        )


def test_symbols_string():
    expected_length = 281
    symbols_string = cmudict.symbols_string()
    actual_length = len(symbols_string)
    if expected_length != actual_length:
        raise AssertionError(
            f"cmudict.symbols_string(): Expected {expected_length} length, got {actual_length}."
        )


def test_vp():
    expected_size = 52
    vp = cmudict.vp()
    actual_size = len(vp)
    if expected_size != actual_size:
        raise AssertionError(
            f"cmudict.vp(): Expected {expected_size} keys, got {actual_size}."
        )


def test_vp_string():
    expected_length = 1747
    vp_string = cmudict.vp_string()
    actual_length = len(vp_string)
    if expected_length != actual_length:
        raise AssertionError(
            f"cmudict.vp_string(): Expected {expected_length} length, got {actual_length}."
        )


def test_vp_comments():
    actual_vp = cmudict.vp()
    expected_vp = {
        "!exclamation-point": [
            [
                "EH2",
                "K",
                "S",
                "K",
                "L",
                "AH0",
                "M",
                "EY1",
                "SH",
                "AH0",
                "N",
                "P",
                "OY2",
                "N",
                "T",
            ]
        ],
        '"close-quote': [["K", "L", "OW1", "Z", "K", "W", "OW1", "T"]],
        '"double-quote': [["D", "AH1", "B", "AH0", "L", "K", "W", "OW1", "T"]],
        '"end-of-quote': [["EH1", "N", "D", "AH0", "V", "K", "W", "OW1", "T"]],
        '"end-quote': [["EH1", "N", "D", "K", "W", "OW1", "T"]],
        '"in-quotes': [["IH1", "N", "K", "W", "OW1", "T", "S"]],
        '"quote': [["K", "W", "OW1", "T"]],
        '"unquote': [["AH1", "N", "K", "W", "OW1", "T"]],
        "#sharp-sign": [["SH", "AA1", "R", "P", "S", "AY1", "N"]],
        "%percent": [["P", "ER0", "S", "EH1", "N", "T"]],
        "&ampersand": [["AE1", "M", "P", "ER0", "S", "AE2", "N", "D"]],
        "(begin-parens": [["B", "IH0", "G", "IH1", "N", "P", "ER0", "EH1", "N", "Z"]],
        "(in-parentheses": [
            ["IH1", "N", "P", "ER0", "EH1", "N", "TH", "AH0", "S", "IY2", "Z"]
        ],
        "(left-paren": [["L", "EH1", "F", "T", "P", "ER0", "EH1", "N"]],
        "(open-parentheses": [
            [
                "OW1",
                "P",
                "AH0",
                "N",
                "P",
                "ER0",
                "EH1",
                "N",
                "TH",
                "AH0",
                "S",
                "IY2",
                "Z",
            ]
        ],
        "(paren": [["P", "ER0", "EH1", "N"]],
        "(parens": [["P", "ER0", "EH1", "N", "Z"]],
        "(parentheses": [["P", "ER0", "EH1", "N", "TH", "AH0", "S", "IY2", "Z"]],
        ")close-paren": [["K", "L", "OW1", "Z", "P", "ER0", "EH1", "N"]],
        ")close-parentheses": [
            ["K", "L", "OW1", "Z", "P", "ER0", "EH1", "N", "TH", "AH0", "S", "IY2", "Z"]
        ],
        ")end-paren": [["EH1", "N", "D", "P", "ER0", "EH1", "N"]],
        ")end-parens": [["EH1", "N", "D", "P", "ER0", "EH1", "N", "Z"]],
        ")end-parentheses": [
            ["EH1", "N", "D", "P", "ER0", "EH1", "N", "TH", "AH0", "S", "IY2", "Z"]
        ],
        ")end-the-paren": [["EH1", "N", "D", "DH", "AH0", "P", "ER0", "EH1", "N"]],
        ")paren": [["P", "ER0", "EH1", "N"]],
        ")parens": [["P", "ER0", "EH1", "N", "Z"]],
        ")right-paren": [
            ["R", "AY1", "T", "P", "ER0", "EH1", "N"],
            ["R", "AY1", "T", "P", "EH1", "R", "AH0", "N"],
        ],
        ")un-parentheses": [
            ["AH1", "N", "P", "ER0", "EH1", "N", "TH", "AH0", "S", "IY1", "Z"]
        ],
        ",comma": [["K", "AA1", "M", "AH0"]],
        "-dash": [["D", "AE1", "SH"]],
        "-hyphen": [["HH", "AY1", "F", "AH0", "N"]],
        "...ellipsis": [["IH0", "L", "IH1", "P", "S", "IH0", "S"]],
        ".decimal": [["D", "EH1", "S", "AH0", "M", "AH0", "L"]],
        ".dot": [["D", "AA1", "T"]],
        ".full-stop": [["F", "UH1", "L", "S", "T", "AA1", "P"]],
        ".period": [["P", "IH1", "R", "IY0", "AH0", "D"]],
        ".point": [["P", "OY1", "N", "T"]],
        "/slash": [["S", "L", "AE1", "SH"]],
        ":colon": [["K", "OW1", "L", "AH0", "N"]],
        ";semi-colon": [
            ["S", "EH1", "M", "IY0", "K", "OW1", "L", "AH0", "N"],
            ["S", "EH1", "M", "IH0", "K", "OW2", "L", "AH0", "N"],
        ],
        "?question-mark": [
            ["K", "W", "EH1", "S", "CH", "AH0", "N", "M", "AA1", "R", "K"]
        ],
        "{brace": [["B", "R", "EY1", "S"]],
        "{left-brace": [["L", "EH1", "F", "T", "B", "R", "EY1", "S"]],
        "{open-brace": [["OW1", "P", "EH0", "N", "B", "R", "EY1", "S"]],
        "}close-brace": [["K", "L", "OW1", "Z", "B", "R", "EY1", "S"]],
        "}right-brace": [["R", "AY1", "T", "B", "R", "EY1", "S"]],
        "'end-inner-quote": [
            ["EH1", "N", "D", "IH1", "N", "ER0", "K", "W", "OW1", "T"]
        ],
        "'end-quote": [["EH1", "N", "D", "K", "W", "OW1", "T"]],
        "'inner-quote": [["IH1", "N", "ER0", "K", "W", "OW1", "T"]],
        "'single-quote": [["S", "IH1", "NG", "G", "AH0", "L", "K", "W", "OW1", "T"]],
        "'quote": [["K", "W", "OW1", "T"]],
        "'apostrophe": [["AH0", "P", "AA1", "S", "T", "R", "AH0", "F", "IY0"]],
    }
    for test_punctuation, expected_pronounciation in expected_vp.items():
        actual_pronounciation = actual_vp[test_punctuation]
        if expected_pronounciation != actual_pronounciation:
            raise AssertionError(
                f"""
                cmudict.vp(): Expected "{expected_pronounciation}", got "{actual_pronounciation}".
                """
            )


def test_license_string():
    expected_length = 1754
    license_string = cmudict.license_string()
    actual_length = len(license_string)
    if expected_length != actual_length:
        raise AssertionError(
            f"cmudict.license_string(): Expected {expected_length} length, got {actual_length}."
        )

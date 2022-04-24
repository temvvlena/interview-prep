from decode import *

className = SubstitutionCipher(encryptWord="It was all a dream.")


def test_convert_unique_string():
    assert className.convert_unique_string() == \
           ['t', 'h', 'e', 'q', 'u', 'i', 'c', 'k', 'o', 'n', 'y', 'x', 'g', 'b', 'l', 'r', 'a', 's', 'w', 'd', 'j',
            'm', 'p', 'v', 'z', 'f']


def test_align_unique_string():
    assert className.align_unique_string() == \
           {'a': 't', 'b': 'h', 'c': 'e', 'd': 'q', 'e': 'u', 'f': 'i', 'g': 'c', 'h': 'k',
            'i': 'o', 'j': 'n', 'k': 'y', 'l': 'x', 'm': 'g', 'n': 'b', 'o': 'l', 'p': 'r',
            'q': 'a', 'r': 's', 's': 'w', 't': 'd', 'u': 'j', 'v': 'm', 'w': 'p', 'x': 'v',
            'y': 'z', 'z': 'f'}


def test_decode():
    assert className.decode_any_string() == "Od ptw txx t qsutg."

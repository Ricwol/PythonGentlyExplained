from exercises.reverse_string import reverseString


def test_reverseString_capitalized():
    assert reverseString('Hello') == 'olleH'


def test_reverseString_empty_string():
    assert reverseString('') == ''


def test_reverseString_lowercase():
    assert reverseString('aaazzz') == 'zzzaaa'


def test_reverseString_same_character():
    assert reverseString('xxxx') == 'xxxx'

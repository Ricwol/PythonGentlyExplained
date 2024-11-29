from exercises.uppercase_letters import getUppercase


def test_getUppercase_capitalized():
    assert getUppercase('Hello') == 'HELLO'


def test_getUppercase_lowercase():
    assert getUppercase('hello') == 'HELLO'


def test_getUppercase_uppercase():
    assert getUppercase('HELLO') == 'HELLO'


def test_getUppercase_special_characters():
    assert getUppercase('Hello, world!') == 'HELLO, WORLD!'


def test_getUppercase_printable_characters():
    assert getUppercase('goodbye 123!') == 'GOODBYE 123!'


def test_getUppercase_numbers():
    assert getUppercase('12345') == '12345'


def test_getUppercase_empty_string():
    assert getUppercase('') == ''

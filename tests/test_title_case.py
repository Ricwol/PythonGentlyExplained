import itertools as it
import random
import string

from exercises.title_case import getTitleCase

random.seed(42)


def test_getTitleCase():
    assert getTitleCase('Hello, world!') == 'Hello, World!'


def test_getTitleCase_uppercase_text():
    assert getTitleCase('HELLO') == 'Hello'


def test_getTitleCase_lowercase_text():
    assert getTitleCase('hello') == 'Hello'


def test_getTitleCase_mixed_case_text():
    assert getTitleCase('hElLo') == 'Hello'


def test_getTitleCase_empty_text():
    assert getTitleCase('') == ''


def test_getTitleCase_separated_by_non_alpha_chars():
    assert getTitleCase('abc123xyz') == 'Abc123Xyz'


def test_getTitleCase_separated_by_space():
    assert getTitleCase('cat dog RAT') == 'Cat Dog Rat'


def test_getTitleCase_separated_by_comma():
    assert getTitleCase('cat,dog,RAT') == 'Cat,Dog,Rat'

 
def test_getTitleCase_random_string():
    chars = list(it.chain(string.ascii_lowercase, string.digits, ' ,.'))

    for _ in range(1000):
        random.shuffle(chars)
        text = ''.join(chars)
        assert getTitleCase(text) == text.title()

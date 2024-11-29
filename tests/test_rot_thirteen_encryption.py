from exercises.rot_thirteen_encryption import rot13


def test_rot13_encryption():
    assert rot13('Hello, world!') == 'Uryyb, jbeyq!'


def test_rot13_decryption():
    assert rot13('Uryyb, jbeyq!') == 'Hello, world!'


def test_rot13_encrypt_decrypt():
    assert rot13(rot13('Hello, world!')) == 'Hello, world!'


def test_rot13_alphabet_shift_lowercase():
    assert rot13('abcdefghijklmnopqrstuvwxyz') == 'nopqrstuvwxyzabcdefghijklm'


def test_rot13_alphabet_shift_uppercase():
    assert rot13('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 'NOPQRSTUVWXYZABCDEFGHIJKLM'


def test_rot13_empty_string():
    assert rot13('') == ''

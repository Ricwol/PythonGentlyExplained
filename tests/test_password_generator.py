import string

from exercises.password_generator import generatePassword


def test_generatePassword_min_length_of_12_chars():
    assert len(generatePassword(8)) == 12


def test_generatePassword_length():
    assert len(generatePassword(14)) == 14


def test_generatePassword_contains_char_from_each_category():
    hasLowercase = False
    hasUppercase = False
    hasNumber = False
    hasSpecial = False

    for character in generatePassword(14):
        if character in string.ascii_lowercase:
            hasLowercase = True

        if character in string.ascii_uppercase:
            hasUppercase = True

        if character in string.digits:
            hasNumber = True

        if character in '~!@#$%^&*()_+':
            hasSpecial = True

    assert hasLowercase and hasUppercase and hasNumber and hasSpecial

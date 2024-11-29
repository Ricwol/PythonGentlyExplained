from exercises.comma_formatted_numbers import commaFormat

def test_commaFormat_one_digit():
    assert commaFormat(1) == '1'

def test_commaFormat_two_digits():
    assert commaFormat(10) == '10'


def test_commaFormat_three_digits():
    assert commaFormat(100) == '100'


def test_commaFormat_four_digits():
    assert commaFormat(1000) == '1,000'


def test_commaFormat_five_digits():
    assert commaFormat(10000) == '10,000'


def test_commaFormat_six_digits():
    assert commaFormat(100000) == '100,000'


def test_commaFormat_seven_digits():
    assert commaFormat(1000000) == '1,000,000'


def test_commaFormat_ten_digits():
    assert commaFormat(1234567890) == '1,234,567,890'


def test_commaFormat_decimal_number():
    assert commaFormat(1000.123456) == '1,000.123456'

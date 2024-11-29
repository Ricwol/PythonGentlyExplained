from exercises.odd_and_even import (
    isEven,
    isOdd
)


def test_isOdd_with_positive_even_number():
    assert isOdd(42) is False


def test_isOdd_with_positive_odd_number():
    assert isOdd(9999) is True


def test_isOdd_with_negative_even_number():
    assert isOdd(-10) is False


def test_isOdd_with_negative_odd_number():
    assert isOdd(-11) is True


def test_isOdd_with_float():
    assert isOdd(3.1415) is False


def test_isEven_with_positive_even_number():
    assert isEven(42) is True


def test_isEven_with_positive_odd_number():
    assert isEven(9999) is False


def test_isEven_with_negative_even_number():
    assert isEven(-10) is True


def test_isEven_with_negative_odd_number():
    assert isEven(-11) is False


def test_isEven_with_float():
    assert isEven(3.1415) is False

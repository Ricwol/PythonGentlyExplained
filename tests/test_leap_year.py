from exercises.leap_year import isLeapYear


def test_isLeapYear_1999():
    assert isLeapYear(1999) is False


def test_isLeapYear_2000():
    assert isLeapYear(2000) is True


def test_isLeapYear_2001():
    assert isLeapYear(2001) is False


def test_isLeapYear_2004():
    assert isLeapYear(2004) is True


def test_isLeapYear_2100():
    assert isLeapYear(2100) is False


def test_isLeapYear_2400():
    assert isLeapYear(2400) is True

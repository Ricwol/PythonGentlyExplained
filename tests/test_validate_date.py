import datetime as dt

from exercises.validate_date import isValidDate


def test_isValidDate_end_of_month():
    assert isValidDate(1999, 12, 31) is True


def test_isValidDate_February_29_leap_year():
    assert isValidDate(2000, 2, 29) is True


def test_isValidDate_February_29_invalid_fail():
    assert isValidDate(2001, 2, 29) is False


def test_isValidDate_invalid_month_fail():
    assert isValidDate(2029, 13, 1) is False


def test_isValidDate_big_year():
    assert isValidDate(1000000, 1, 1) is True


def test_isValidDate_invalid_day_for_April_fail():
    assert isValidDate(2015, 4, 31) is False


def test_isValidDate_day_out_of_bounds_fail():
    assert isValidDate(1970, 5, 99) is False


def test_isValidDate_month_0_fail():
    assert isValidDate(1981, 0, 3) is False


def test_isValidDate_day_0_fail():
    assert isValidDate(1666, 4, 0) is False


def test_isValidDate_incrementally():
    date = dt.date(1970, 1, 1)
    oneDay = dt.timedelta(days=1)

    for _ in range(1000000):
        assert isValidDate(date.year, date.month, date.day) is True
        date += oneDay

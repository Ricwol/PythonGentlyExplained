from exercises.hours_minutes_seconds import getHoursMinutesSeconds


def test_getHoursMinutesSeconds_30s():
    assert getHoursMinutesSeconds(30) == '30s'

def test_getHoursMinutesSeconds_1m():
    assert getHoursMinutesSeconds(60) == '1m'

def test_getHoursMinutesSeconds_1m_30s():
    assert getHoursMinutesSeconds(90) == '1m 30s'

def test_getHoursMinutesSeconds_1h():
    assert getHoursMinutesSeconds(3600) == '1h'

def test_getHoursMinutesSeconds_1h_1s():
    assert getHoursMinutesSeconds(3601) == '1h 1s'

def test_getHoursMinutesSeconds_1h_1m_1s():
    assert getHoursMinutesSeconds(3661) == '1h 1m 1s'

def test_getHoursMinutesSeconds_25h_42s():
    assert getHoursMinutesSeconds(90042) == '25h 42s'

def test_getHoursMinutesSeconds_0s():
    assert getHoursMinutesSeconds(0) == '0s'

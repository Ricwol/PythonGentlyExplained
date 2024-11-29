from exercises.change_maker import makeChange


def test_makeChange_30():
    assert makeChange(30) == {'quarters': 1, 'nickels': 1}


def test_makeChange_one_dime():
    assert makeChange(10) == {'dimes': 1}


def test_makeChange_loose_change():
    assert makeChange(57) == {'quarters': 2, 'nickels': 1, 'pennies': 2}


def test_makeChange_100():
    assert makeChange(100) == {'quarters': 4}


def test_makeChange_5_quarters():
    assert makeChange(125) == {'quarters': 5}

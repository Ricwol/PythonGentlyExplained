from exercises.ordinal_suffix import ordinalSuffix


def test_ordinalSuffix_0th():
    assert ordinalSuffix(0) == '0th'


def test_ordinalSuffix_1st():
    assert ordinalSuffix(1) == '1st'


def test_ordinalSuffix_2nd():
    assert ordinalSuffix(2) == '2nd'


def test_ordinalSuffix_3rd():
    assert ordinalSuffix(3) == '3rd'


def test_ordinalSuffix_4th():
    assert ordinalSuffix(4) == '4th'


def test_ordinalSuffix_10th():
    assert ordinalSuffix(10) == '10th'


def test_ordinalSuffix_11th():
    assert ordinalSuffix(11) == '11th'


def test_ordinalSuffix_12th():
    assert ordinalSuffix(12) == '12th'


def test_ordinalSuffix_13th():
    assert ordinalSuffix(13) == '13th'


def test_ordinalSuffix_14th():
    assert ordinalSuffix(14) == '14th'


def test_ordinalSuffix_101st():
    assert ordinalSuffix(101) == '101st'

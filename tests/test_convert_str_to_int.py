from exercises.convert_str_to_int import convertStrToInt


def test_convertStrToInt():
    for i in range(-10000, 10000):
        assert convertStrToInt(str(i)) == i

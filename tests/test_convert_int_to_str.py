from exercises.convert_int_to_str import convertIntToStr


def test_convertIntToStr():
    for i in range(-10000, 10000):
        assert convertIntToStr(i) == str(i)

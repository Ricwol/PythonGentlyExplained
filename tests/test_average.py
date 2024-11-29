import random

from exercises.average import average

random.seed(42)


def test_average():
    assert average([1, 2, 3]) == 2.0


def test_average_repeated_numbers():
    assert average([1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2.0


def test_average_big_numbers_ascending():
    assert average([12, 20, 37]) == 23.0


def test_average_zeros():
    assert average([0, 0, 0, 0, 0]) == 0.0


def test_average_empty_list():
    assert average([]) is None


def test_average_random_order():
    testData = [1, 2, 3, 1, 2, 3, 1, 2, 3]

    for _ in range(1000):
        random.shuffle(testData)
        assert average(testData) == 2.0

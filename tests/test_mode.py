import random

from exercises.mode import mode

random.seed(42)


def test_mode_empty_list():
    assert mode([]) is None


def test_mode_last_number():
    assert mode([1, 2, 3, 4, 4]) == 4


def test_mode_first_number():
    assert mode([1, 1, 2, 3, 4]) == 1


def test_mode_random_order():
    testData = [1, 2, 3, 4, 4]

    for _ in range(1000):
        random.shuffle(testData)
        assert mode(testData) == 4

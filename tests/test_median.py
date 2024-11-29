import random

from exercises.median import median

random.seed(42)


def test_median_empty_list():
    assert median([]) is None


def test_median_ascending_order_odd_length():
    assert median([1, 2, 3]) == 2


def test_median_unordered_even_length():
    assert median([3, 7, 10, 4, 1, 9, 6, 5, 2, 8]) == 5.5


def test_median_unordered_odd_length():
    assert median([3, 7, 10, 4, 1, 9, 6, 2, 8]) == 6


def test_median_random_order():
    testData = [3, 7, 10, 4, 1, 9, 6, 2, 8]

    for _ in range(1000):
        random.shuffle(testData)
        assert median(testData) == 6

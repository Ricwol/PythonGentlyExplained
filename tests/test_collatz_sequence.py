import random

from exercises.collatz_sequence import collatz

random.seed(42)


def test_collatz_startingNumber_less_than_1():
    assert collatz(0) == []


def test_collatz_startingNumber_10():
    assert collatz(10) == [10, 5, 16, 8, 4, 2, 1]


def test_collatz_startingNumber_11():
    assert collatz(11) == [11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]


def test_collatz_startingNumber_12():
    assert collatz(12) == [12, 6, 3, 10, 5, 16, 8, 4, 2, 1]


def test_collatz_startingNumber_length_256():
    assert len(collatz(256)) == 9


def test_collatz_startingNumber_length_257():
    assert len(collatz(257)) == 123


def test_collatz_startingNumber_random_value():
    for _ in range(1000):
        startingNum = random.randint(1, 10000)
        seq = collatz(startingNum)
        assert seq[0] == startingNum
        assert seq[-1] == 1

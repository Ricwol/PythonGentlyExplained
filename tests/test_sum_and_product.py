from exercises.sum_and_product import (
    calculateProduct,
    calculateSum
)

def test_calculateSum_empty_list():
    assert calculateSum([]) == 0


def test_calculateSum():
    assert calculateSum([2, 4, 6, 8, 10]) == 30


def test_calculateProduct_empty_list():
    assert calculateProduct([]) == 1


def test_calculateProduct():
    assert calculateProduct([2, 4, 6, 8, 10]) == 3840

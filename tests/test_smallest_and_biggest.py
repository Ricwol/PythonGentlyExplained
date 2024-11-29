from exercises.smallest_and_biggest import getSmallest


def test_getSmallest_ascending_order():
    assert getSmallest([1, 2, 3]) == 1


def test_getSmallest_descending_order():
    assert getSmallest([3, 2, 1]) == 1


def test_smallest_arbitrary_order():
    assert getSmallest([28, 25, 42, 2, 28]) == 2


def test_getSmallest_one_element_list():
    assert getSmallest([1]) == 1


def test_getSmallest_empty_list():
    assert getSmallest([]) is None

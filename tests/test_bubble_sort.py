from exercises.bubble_sort import bubbleSort


def test_bubbleSort_empty_list():
    assert bubbleSort([]) == []


def test_bubbleSort_in_place():
    numbers = [2, 0, 4, 1, 3]
    bubbleSort(numbers)
    assert numbers == [0, 1, 2, 3, 4]


def test_bubbleSort():
    assert bubbleSort([2, 0, 4, 1, 3]) == [0, 1, 2, 3, 4]


def test_bubbleSort_same_number():
    assert bubbleSort([2, 2, 2, 2]) == [2, 2, 2, 2]


def test_bubbleSort_ascending_order_input():
    assert bubbleSort([0, 1, 2, 3, 4]) == [0, 1, 2, 3, 4]


def test_bubbleSort_descending_order_input():
    assert bubbleSort([4, 3, 2, 1, 0]) == [0, 1, 2, 3, 4]

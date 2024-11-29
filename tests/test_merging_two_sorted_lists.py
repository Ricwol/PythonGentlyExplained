from exercises.merging_two_sorted_lists import mergeTwoLists


def test_mergeTwoLists_of_odd_numbers():
    assert mergeTwoLists([1, 3, 6], [5, 7, 8, 9]) == [1, 3, 5, 6, 7, 8, 9]


def test_mergeTwoLists_already_sorted():
    assert mergeTwoLists([1, 2, 3], [4, 5]) == [1, 2, 3, 4, 5]


def test_mergeTwoLists_reverse_order():
    assert mergeTwoLists([4, 5], [1, 2, 3]) == [1, 2, 3, 4, 5]


def test_mergeTwoLists_same_value():
    assert mergeTwoLists([2, 2, 2], [2, 2, 2]) == [2, 2, 2, 2, 2, 2]


def test_mergeTwoLists_merge_empty_list2():
    assert mergeTwoLists([1, 2, 3], []) == [1, 2, 3]


def test_mergeTwoLists_merge_empty_list1():
    assert mergeTwoLists([], [1, 2, 3]) == [1, 2, 3]


def test_mergeTwoLists_merge_empty_lists():
    assert mergeTwoLists([], []) == []

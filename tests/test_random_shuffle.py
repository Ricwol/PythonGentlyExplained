from exercises.random_shuffle import shuffle


def test_shuffle_length():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    shuffle(data)
    assert len(data) == 10


def test_shuffle_unshuffle_to_original_order():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    shuffle(data)
    assert data != [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert sorted(data) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

 
def test_shuffle_empty_list():
    data = []
    shuffle(data)
    assert data == []

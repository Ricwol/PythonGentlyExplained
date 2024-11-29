from exercises.handshakes import printHandshakes


def test_printHandshakes_nobody():
    assert printHandshakes([]) == 0


def test_printHandshakes_single_person():
    assert printHandshakes(['Alice']) == 0


def test_printHandshakes_between_two_people():
    assert printHandshakes(['Alice', 'Bob']) == 1


def test_printHandshakes_between_three_people():
    assert printHandshakes(['Alice', 'Bob', 'Carol']) == 3


def test_printHandshakes_between_four_people():
    assert printHandshakes(['Alice', 'Bob', 'Carol', 'David']) == 6

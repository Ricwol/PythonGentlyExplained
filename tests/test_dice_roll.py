from exercises.dice_roll import rollDice


def test_rollDice_0():
    assert rollDice(0) == 0


def test_rollDice_1000_dice():
    assert rollDice(1000) != rollDice(1000)


def test_rollDice_range_with_various_number_of_dice():
    for _ in range(1000):
        assert 1 <= rollDice(1) <= 6
        assert 2 <= rollDice(2) <= 12
        assert 3 <= rollDice(3) <= 18
        assert 100 <= rollDice(100) <= 600

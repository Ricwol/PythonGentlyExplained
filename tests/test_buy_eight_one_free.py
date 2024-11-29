from exercises.buy_eight_one_free import getCostOfCoffee


def test_getCostOfCoffee_below_8_coffee():
    assert getCostOfCoffee(7, 2.50) == 17.50


def test_getCostOfCoffee_exactly_8_coffee():
    assert getCostOfCoffee(8, 2.50) == 20


def test_getCostOfCoffee_9_coffee():
    assert getCostOfCoffee(9, 2.50) == 20


def test_getCostOfCoffee_10_coffee():
    assert getCostOfCoffee(10, 2.50) == 22.50


def test_getCostOfCoffee_various_prices():
    for i in range(1, 4):
        assert getCostOfCoffee(0, i) == 0
        assert getCostOfCoffee(8, i) == 8*i
        assert getCostOfCoffee(9, i) == 8*i
        assert getCostOfCoffee(18, i) == 16*i
        assert getCostOfCoffee(19, i) == 17*i
        assert getCostOfCoffee(30, i) == 27*i

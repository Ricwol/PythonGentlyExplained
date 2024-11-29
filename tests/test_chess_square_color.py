from exercises.chess_square_color import getChessSquareColor


def test_getChessSquareColor_white_0_0():
    assert getChessSquareColor(0, 0) == 'white'


def test_getChessSquareColor_black_1_0():
    assert getChessSquareColor(1, 0) == 'black'

def test_getChessSquareColor_black_0_1():
    assert getChessSquareColor(0, 1) == 'black'


def test_getChessSquareColor_white_7_7():
    assert getChessSquareColor(7, 7) == 'white'


def test_getChessSquareColor_row_out_of_bounds_empty():
    assert getChessSquareColor(0, 8) == ''


def test_getChessSquareColor_column_out_of_bounds_empty():
    assert getChessSquareColor(9, 2) == ''


def test_getChessSquareColor_out_of_bounds():
    assert getChessSquareColor(-1, 10) == ''

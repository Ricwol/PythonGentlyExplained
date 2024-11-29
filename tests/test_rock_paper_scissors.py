from exercises.rock_paper_scissors import rpsWinner


def test_rpsWinner_rock_loses_to_paper():
    assert rpsWinner('rock', 'paper') == 'player two'


def test_rpsWinner_rock_beats_scissors():
    assert rpsWinner('rock', 'scissors') == 'player one'


def test_rpsWinner_paper_loses_to_scissors():
    assert rpsWinner('paper', 'scissors') == 'player two'


def test_rpsWinner_paper_beats_rock():
    assert rpsWinner('paper', 'rock') == 'player one'


def test_rpsWinner_scissors_loses_to_rock():
    assert rpsWinner('scissors', 'rock') == 'player two'


def test_rpsWinner_scissors_beats_paper():
    assert rpsWinner('scissors', 'paper') == 'player one'


def test_rpsWinner_tie():
    assert rpsWinner('rock', 'rock') == 'tie'
    assert rpsWinner('paper', 'paper') == 'tie'
    assert rpsWinner('scissors', 'scissors') == 'tie'

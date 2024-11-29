from exercises.find_and_replace import findAndReplace


def test_findAndReplace_oldText_in_text():
    assert findAndReplace('The fox', 'fox', 'dog') == 'The dog'


def test_findAndReplace_oldText_is_text():
    assert findAndReplace('fox', 'fox', 'dog') == 'dog'


def test_findAndReplace_oldText_is_substring():
    assert findAndReplace('Firefox', 'fox', 'dog') == 'Firedog'


def test_findAndReplace_multiple_substrings():
    assert findAndReplace('foxfox', 'fox', 'dog') == 'dogdog'


def test_findAndReplace_case_sensitive():
    assert findAndReplace('The Fox and fox.', 'fox', 'dog') == 'The Fox and dog.'

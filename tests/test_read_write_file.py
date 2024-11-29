import pytest

from exercises.read_write_file import (
    appendToFile,
    readFromFile,
    writeToFile
)


@pytest.fixture(scope='session')
def greet_file(tmp_path_factory):
    file = tmp_path_factory.mktemp('sub') / 'greet.txt'
    return file


def test_writeToFile(greet_file):
    writeToFile(greet_file, text='Hello!\n')
    assert greet_file.read_text() == 'Hello!\n'


def test_appendToFile(greet_file):    
    appendToFile(greet_file, text='Goodbye!\n')
    assert greet_file.read_text() == 'Hello!\nGoodbye!\n'


def test_readFromFile(greet_file):
    assert 'Hello!\nGoodbye!\n' == readFromFile(greet_file)

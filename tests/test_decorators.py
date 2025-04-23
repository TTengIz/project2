from src.decorators import log
import pytest


@log(filename="mylog.txt")
def my_function(x: int, y: int) -> int:
    return x + y

def test_log_success():
    assert my_function(3, 1) == 4


def test_log_error():
    with pytest.raises(TypeError):
        my_function(3 , '1')

@log()
def add(x: int, y: int) -> int:
    return x + y


def test_log_cansol(capsys):
    add(1, 2)
    captured = capsys.readouterr()
    assert 'ok time for work' in captured.out

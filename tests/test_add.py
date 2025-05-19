# tests/test_add.py
import pytest
from add import add

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-1, -1) == -2

def test_add_zero():
    assert add(0, 5) == 5
    assert add(5, 0) == 5

@pytest.mark.parametrize("a,b,expected", [
    (1, 1, 2),
    (-2, 4, 2),
    (3, -3, 0),
    (1.5, 2.5, 4.0),
])
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected

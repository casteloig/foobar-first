import pytest

from src.maths import funcs as f


@pytest.mark.parametrize("input,expected", [(1, 1), (5, 120), (-1, "NAN"), (0, "NAN")])
def test_factorial(input, expected):
    assert f.factorial(input) == expected


@pytest.mark.parametrize("input,expected", [(1, 0), (5, 3), (-1, "NAN"), (0, "NAN")])
def test_fibonacci(input, expected):
    assert f.fib(input) == expected

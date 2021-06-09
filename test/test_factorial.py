import pytest
import sys
sys.path.append('../src/factorial')
import func_factorial as f

@pytest.mark.parametrize(
    "input,expected",
    [
        (1,1),
        (5,120),
        (-1,"NAN"),
        (0, "NAN")
    ]
)
def test_factorial(input,expected):
    assert f.factorial(input) == expected

import pytest
from calculator.operations import Operations


@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 8),
    (-5, 3, -2),
    (1.5, 2.5, 4),
    (0, 0, 0),
])
def test_add(a, b, expected):
    assert Operations.add(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (10, 3, 7),
    (-5, 3, -8),
    (2.5, 1.5, 1),
    (0, 0, 0),
])
def test_subtract(a, b, expected):
    assert Operations.subtract(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 15),
    (-5, 3, -15),
    (2.5, 2, 5),
    (0, 10, 0),
])
def test_multiply(a, b, expected):
    assert Operations.multiply(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (-10, 2, -5),
    (2.5, 2, 1.25),
    (0, 5, 0),
])
def test_divide(a, b, expected):
    assert Operations.divide(a, b) == expected


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        Operations.divide(10, 0)

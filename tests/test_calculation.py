import pytest

from calculator.calculation import Calculation, ArithmeticCalculation
from calculator.operations import Operations


def test_factory_creates_calculation():
    calc = ArithmeticCalculation.create(10, 5, Operations.add)

    assert isinstance(calc, ArithmeticCalculation)
    assert calc.a == 10
    assert calc.b == 5
    assert calc.operation == Operations.add
    assert calc.execute() == 15


def test_abstract_class_cannot_be_instantiated():
    with pytest.raises(TypeError):
        Calculation(10, 5, Operations.add)


@pytest.mark.parametrize("operation, a, b, expected", [
    (Operations.add, 10, 5, 15),
    (Operations.subtract, 10, 5, 5),
    (Operations.multiply, 10, 5, 50),
    (Operations.divide, 10, 5, 2),
])
def test_calculation_operations(operation, a, b, expected):
    calc = ArithmeticCalculation.create(a, b, operation)

    assert calc.execute() == expected

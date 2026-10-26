import pytest

from calculator.operations import Operations
from calculator.calculation import ArithmeticCalculation
from calculator.commands import CalculateCommand, HistoryCommand


def test_calculate_command():
    history = []

    calc = ArithmeticCalculation.create(5, 3, Operations.add)
    command = CalculateCommand(calc, history)

    result = command.execute()

    assert result == 8
    assert history == ["add 5 3 = 8"]


def test_multiple_calculations():
    history = []

    calc1 = ArithmeticCalculation.create(10, 5, Operations.subtract)
    calc2 = ArithmeticCalculation.create(4, 3, Operations.multiply)

    CalculateCommand(calc1, history).execute()
    CalculateCommand(calc2, history).execute()

    assert len(history) == 2
    assert history[0] == "subtract 10 5 = 5"
    assert history[1] == "multiply 4 3 = 12"


def test_failed_calculation_not_saved():
    history = []

    calc = ArithmeticCalculation.create(10, 0, Operations.divide)
    command = CalculateCommand(calc, history)

    with pytest.raises(ValueError, match="Cannot divide by zero"):
        command.execute()

    assert history == []


def test_empty_history():
    history = []

    command = HistoryCommand(history)

    assert command.execute() == []


def test_history_returns_copy():
    history = ["add 5 3 = 8"]

    command = HistoryCommand(history)

    result = command.execute()

    # Changing the returned list must not change the original history.
    result.append("subtract 10 5 = 5")

    assert len(result) == 2
    assert len(history) == 1
    assert history == ["add 5 3 = 8"]

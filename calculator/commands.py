from .calculation import Calculation


class CalculateCommand:
    def __init__(self, calculation: Calculation, history: list[str]):
        # Store the calculation and shared history.
        self.calculation = calculation
        self.history = history

    def execute(self) -> float:
        # Execute the calculation.
        result = self.calculation.execute()

        # Save only successful calculations.
        entry = (
            f"{self.calculation.operation.__name__} "
            f"{self.calculation.a} {self.calculation.b} = {result}"
        )
        self.history.append(entry)

        return result


class HistoryCommand:
    def __init__(self, history: list[str]):
        self.history = history

    def execute(self) -> list[str]:
        # Return a copy to protect the original history.
        return self.history.copy()

from .operations import Operations
from .calculation import ArithmeticCalculation
from .commands import CalculateCommand, HistoryCommand


def main():
    history = []

    # Strategy pattern: select an operation using a dictionary.
    operations = {
        "add": Operations.add,
        "subtract": Operations.subtract,
        "multiply": Operations.multiply,
        "divide": Operations.divide,
    }

    print("Welcome to the CLI Calculator!")
    print("Commands: add, subtract, multiply, divide, history, exit")

    while True:
        try:
            user_input = input("> ")
        except EOFError:
            print("\nGoodbye!")
            break

        parts = user_input.strip().split()

        if not parts:
            continue

        command_name = parts[0].lower()

        if command_name == "exit":
            print("Goodbye!")
            break

        if command_name == "history":
            if len(parts) != 1:
                print("Usage: history")
                continue

            entries = HistoryCommand(history).execute()

            if not entries:
                print("History is empty.")
            else:
                for entry in entries:
                    print(entry)

            continue

        if command_name not in operations:
            print("Unknown command.")
            continue

        if len(parts) != 3:
            print("Please enter exactly two numbers.")
            continue

        try:
            a = float(parts[1])
            b = float(parts[2])
        except ValueError:
            print("Invalid number.")
            continue

        try:
            # Read command -> select strategy -> create calculation
            # -> execute command -> print result.
            operation = operations[command_name]

            calculation = ArithmeticCalculation.create(
                a, b, operation
            )

            command = CalculateCommand(calculation, history)

            result = command.execute()

            print(result)

        except ValueError as error:
            print(error)

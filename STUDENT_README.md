# CLI Calculator Project

This project is a command-line calculator built using Python. It supports addition, subtraction, multiplication, and division. It also keeps a history of successful calculations.

The project demonstrates Object-Oriented Programming (OOP), SOLID principles, and the Factory, Command, and Strategy design patterns.

## Setup, Run, and Test

The project requires Python 3.12 or newer.

### 1. Create a virtual environment

```powershell
python -m venv .venv
```

### 2. Activate the environment (Windows)

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 4. Run the calculator

```powershell
python -m calculator
```

### 5. Run automated tests

```powershell
python -m pytest --cov=calculator --cov-report=term-missing --cov-fail-under=100
```

## Example Conversation

The calculator accepts commands until the user types `exit`.

```text
Welcome to the CLI Calculator!
Commands: add, subtract, multiply, divide, history, exit

> add 5 3
8.0

> subtract 10 4
6.0

> multiply 6 3
18.0

> divide 10 2
5.0

> divide 10 0
Cannot divide by zero

> history
add 5.0 3.0 = 8.0
subtract 10.0 4.0 = 6.0
multiply 6.0 3.0 = 18.0
divide 10.0 2.0 = 5.0

> exit
Goodbye!
```

Failed calculations are not added to history.

## Static, Class, and Instance Methods

**Static Methods:**

The `Operations` class uses static methods for addition, subtraction, multiplication, and division. These methods do not need an object because they only work with the numbers provided.

**Class Methods:**

The `create()` method in the `Calculation` class is a class method. It uses `cls` to create a new calculation object. The `ArithmeticCalculation` class inherits this method.

**Instance Methods:**

The `execute()` method in `ArithmeticCalculation` is an instance method. It uses `self` to access the stored numbers and operation and then returns the result.

## Factory, Command, and Strategy Patterns

### Factory Pattern

The Factory pattern is implemented using `ArithmeticCalculation.create()`.

Instead of creating the calculation directly, the factory method creates an object with the two numbers and the selected operation.

### Command Pattern

The Command pattern is implemented using `CalculateCommand` and `HistoryCommand`.

`CalculateCommand` executes a calculation and adds successful results to history.

`HistoryCommand` returns a copy of the calculation history.

### Strategy Pattern

The Strategy pattern is implemented using a dictionary of operations in `cli.py`.

Each operation is a different strategy. The program selects the correct operation based on the user's command.

For example, when the user enters `add 5 3`:

1. The CLI reads the input.
2. The dictionary selects `Operations.add`.
3. `ArithmeticCalculation.create()` creates the calculation object.
4. `CalculateCommand` receives the calculation.
5. The command calls `execute()`.
6. The result is displayed and saved in history.

The same process works for subtraction, multiplication, and division without changing the calculation execution code.

## Object-Oriented Programming (OOP)

### Encapsulation

Encapsulation means keeping related data and behavior together.

The `Calculation` class stores the numbers and operation inside an object. The `HistoryCommand` also protects the original history by returning a copy instead of the actual list.

### Abstraction

Abstraction means defining what an object should do without providing all the implementation details.

The abstract `Calculation` class requires an `execute()` method. The `ArithmeticCalculation` class provides the actual implementation.

### Inheritance

Inheritance allows a class to reuse functionality from another class.

`ArithmeticCalculation` inherits from `Calculation`, including the `create()` factory method.

### Polymorphism

Polymorphism allows different objects to follow the same interface.

`CalculateCommand` works with the `Calculation` abstraction. Different concrete calculation classes can provide their own `execute()` implementation while following the same contract.

### Composition

Composition means building objects using other objects.

`CalculateCommand` contains a calculation object, and the calculation object contains an operation function.

This separates the responsibilities of each part.

## SOLID Principles

### 1. Single Responsibility Principle

Each class has one main responsibility.

For example, `Operations` handles arithmetic, `CalculateCommand` executes calculations and records history, and `cli.py` handles user input and output.

### 2. Open/Closed Principle

The calculator can be extended with new operations without changing the existing calculation execution logic.

For example, to add another arithmetic operation, we can create a new static method in `Operations` and register it in the CLI operation dictionary.

The `ArithmeticCalculation.execute()` method does not need to change.

### 3. Liskov Substitution Principle

A subclass should be able to replace its parent class without breaking the program.

Any concrete subclass of `Calculation` should follow the same `execute()` contract by returning a numeric result or raising an appropriate error.

### 4. Interface Segregation Principle

Classes should not be forced to implement methods they do not need.

The `Calculation` abstract class only requires the `execute()` method, keeping the interface small and simple.

### 5. Dependency Inversion Principle

Higher-level classes should depend on abstractions rather than specific implementations.

`CalculateCommand` accepts a `Calculation` object instead of depending directly on a specific arithmetic operation.

The operation is also passed into the calculation rather than being hard-coded.

## Tests and GitHub Actions

The project uses `pytest` and `pytest-cov` for automated testing.

Tests cover:

* All four arithmetic operations
* Negative numbers, decimals, and zero
* Division by zero
* Factory object creation
* Abstract class behavior
* Calculation execution
* Command execution
* Successful and failed calculation history
* Invalid commands and operands
* CLI exit and EOF behavior

The project achieves **100% line coverage** across the calculator package.

GitHub Actions automatically runs the tests on pushes and pull requests and requires 100% coverage.

**Successful GitHub Actions Run:**

https://github.com/mmm286masud/is218-calculator-patterns/actions/runs/40369234224

## Coverage Exclusions

The abstract `Calculation.execute()` placeholder uses `# pragma: no cover` because it only defines the required method and does not perform any calculation.

The entry-point condition in `__main__.py` also uses `# pragma: no cover` because it is a small startup guard. The calculator's actual functionality and entry point are tested separately.

No arithmetic operations, calculations, commands, history handling, or CLI error handling are excluded from coverage.

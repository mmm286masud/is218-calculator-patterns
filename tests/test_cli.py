from calculator.cli import main


def test_cli_commands_and_history(monkeypatch, capsys):
    inputs = iter([
        "",
        "history",
        "history extra",
        "unknown 5 3",
        "add 5",
        "add 5 3 2",
        "add abc 3",
        "divide 10 0",
        "add 5 3",
        "subtract -5 2",
        "multiply 1.5 2",
        "divide 6 3",
        "history",
        "exit",
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main()

    output = capsys.readouterr().out

    # Check welcome message.
    assert "Welcome to the CLI Calculator!" in output

    # Check empty history.
    assert "History is empty." in output

    # Check invalid commands and inputs.
    assert "Usage: history" in output
    assert "Unknown command." in output
    assert output.count("Please enter exactly two numbers.") == 2
    assert "Invalid number." in output
    assert "Cannot divide by zero" in output

    # Check successful calculations.
    assert "8.0" in output
    assert "-7.0" in output
    assert "3.0" in output
    assert "2.0" in output

    # Check calculation history.
    assert "add 5.0 3.0 = 8.0" in output
    assert "subtract -5.0 2.0 = -7.0" in output
    assert "multiply 1.5 2.0 = 3.0" in output
    assert "divide 6.0 3.0 = 2.0" in output

    # Failed calculations should not appear in history.
    assert "divide 10.0 0.0 =" not in output

    # Check history order.
    assert output.index("add 5.0 3.0 = 8.0") < output.index(
        "subtract -5.0 2.0 = -7.0"
    )

    # Check exit.
    assert "Goodbye!" in output


def test_cli_eof(monkeypatch, capsys):
    def fake_input(prompt):
        raise EOFError

    monkeypatch.setattr("builtins.input", fake_input)

    main()

    output = capsys.readouterr().out

    assert "Goodbye!" in output


def test_main_entry_point(monkeypatch, capsys):
    import runpy

    monkeypatch.setattr("builtins.input", lambda _: "exit")

    runpy.run_module("calculator", run_name="__main__")

    output = capsys.readouterr().out

    assert "Welcome to the CLI Calculator!" in output
    assert "Goodbye!" in output

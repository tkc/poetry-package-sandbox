"""Tests for the CLI module."""

import pytest
from simple_calculator.cli import main


def test_cli_add(capsys):
    """Test the CLI add operation."""
    main(["add", "2", "3"])
    captured = capsys.readouterr()
    assert "Result: 5.0" in captured.out


def test_cli_subtract(capsys):
    """Test the CLI subtract operation."""
    main(["subtract", "5", "3"])
    captured = capsys.readouterr()
    assert "Result: 2.0" in captured.out


def test_cli_multiply(capsys):
    """Test the CLI multiply operation."""
    main(["multiply", "2", "3"])
    captured = capsys.readouterr()
    assert "Result: 6.0" in captured.out


def test_cli_divide(capsys):
    """Test the CLI divide operation."""
    main(["divide", "6", "3"])
    captured = capsys.readouterr()
    assert "Result: 2.0" in captured.out


def test_cli_sqrt(capsys):
    """Test the CLI sqrt operation."""
    main(["sqrt", "9"])
    captured = capsys.readouterr()
    assert "Result: 3.0" in captured.out


def test_cli_pow(capsys):
    """Test the CLI pow operation."""
    main(["pow", "2", "3"])
    captured = capsys.readouterr()
    assert "Result: 8.0" in captured.out


def test_cli_log(capsys):
    """Test the CLI log operation."""
    main(["log", "100", "10"])
    captured = capsys.readouterr()
    assert "Result: 2.0" in captured.out


def test_cli_log_default_base(capsys):
    """Test the CLI log operation with default base."""
    main(["log", "100"])
    captured = capsys.readouterr()
    assert "Result: 2.0" in captured.out  # log_10(100) = 2


def test_cli_error_handling(capsys):
    """Test the CLI error handling."""
    with pytest.raises(SystemExit):
        main(["divide", "5", "0"])

    captured = capsys.readouterr()
    assert "Error: Cannot divide by zero" in captured.out

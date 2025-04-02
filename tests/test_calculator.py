"""Tests for the Calculator class."""

import math

import pytest
from simple_calculator import Calculator


class TestCalculator:
    """Test cases for the Calculator class."""

    def setup_method(self):
        """Set up a calculator instance for each test."""
        self.calculator = Calculator()

    def test_add(self):
        """Test the add method."""
        assert self.calculator.add(2, 3) == 5
        assert self.calculator.add(-1, 1) == 0
        assert self.calculator.add(0, 0) == 0
        assert self.calculator.add(1.5, 2.5) == 4.0

    def test_subtract(self):
        """Test the subtract method."""
        assert self.calculator.subtract(5, 3) == 2
        assert self.calculator.subtract(1, 1) == 0
        assert self.calculator.subtract(0, 5) == -5
        assert self.calculator.subtract(10.5, 0.5) == 10.0

    def test_multiply(self):
        """Test the multiply method."""
        assert self.calculator.multiply(2, 3) == 6
        assert self.calculator.multiply(-2, 3) == -6
        assert self.calculator.multiply(0, 5) == 0
        assert self.calculator.multiply(2.5, 2) == 5.0

    def test_divide(self):
        """Test the divide method."""
        assert self.calculator.divide(6, 3) == 2.0
        assert self.calculator.divide(5, 2) == 2.5
        assert self.calculator.divide(0, 5) == 0.0
        assert self.calculator.divide(-6, 2) == -3.0

    def test_divide_by_zero(self):
        """Test division by zero raises an error."""
        with pytest.raises(ZeroDivisionError):
            self.calculator.divide(5, 0)

    def test_square_root(self):
        """Test the square_root method."""
        assert self.calculator.square_root(9) == 3.0
        assert self.calculator.square_root(2) == pytest.approx(1.4142, 0.0001)
        assert self.calculator.square_root(0) == 0.0

    def test_square_root_negative(self):
        """Test square root of negative number raises an error."""
        with pytest.raises(
            ValueError, match="Cannot calculate square root of a negative number"
        ):
            self.calculator.square_root(-1)

    def test_power(self):
        """Test the power method."""
        assert self.calculator.power(2, 3) == 8
        assert self.calculator.power(3, 2) == 9
        assert self.calculator.power(5, 0) == 1
        assert self.calculator.power(0, 5) == 0
        assert self.calculator.power(2, -1) == 0.5

    def test_log(self):
        """Test the log method."""
        assert self.calculator.log(100, 10) == 2.0
        assert self.calculator.log(8, 2) == 3.0
        assert self.calculator.log(math.e) == 1.0  # Natural log of e is 1

    def test_log_invalid(self):
        """Test log of invalid inputs raises errors."""
        with pytest.raises(
            ValueError, match="Cannot calculate logarithm of a non-positive number"
        ):
            self.calculator.log(0)  # Log of 0 is undefined

        with pytest.raises(
            ValueError, match="Cannot calculate logarithm of a non-positive number"
        ):
            self.calculator.log(-1)  # Log of negative number is undefined

        with pytest.raises(ValueError, match="Invalid logarithm base"):
            self.calculator.log(10, 0)  # Base must be positive

        with pytest.raises(ValueError, match="Invalid logarithm base"):
            self.calculator.log(10, 1)  # Base cannot be 1

    def test_last_result(self):
        """Test the last_result property."""
        assert self.calculator.get_last_result() is None  # Initially None

        self.calculator.add(2, 3)
        assert self.calculator.get_last_result() == 5

        self.calculator.subtract(10, 4)
        assert self.calculator.get_last_result() == 6

        self.calculator.multiply(2, 3)
        assert self.calculator.get_last_result() == 6

        self.calculator.divide(10, 2)
        assert self.calculator.get_last_result() == 5.0

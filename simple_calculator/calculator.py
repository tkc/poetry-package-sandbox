"""Calculator module providing basic and scientific arithmetic operations."""

import math
from typing import Union, Optional

Number = Union[int, float]


class Calculator:
    """A simple calculator with basic and scientific operations."""

    def __init__(self) -> None:
        """Initialize the calculator."""
        self.last_result: Optional[Number] = None

    def add(self, a: Number, b: Number) -> Number:
        """Add two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            The sum of a and b
        """
        self.last_result = a + b
        return self.last_result

    def subtract(self, a: Number, b: Number) -> Number:
        """Subtract b from a.

        Args:
            a: First number
            b: Second number

        Returns:
            The result of a - b
        """
        self.last_result = a - b
        return self.last_result

    def multiply(self, a: Number, b: Number) -> Number:
        """Multiply two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            The product of a and b
        """
        self.last_result = a * b
        return self.last_result

    def divide(self, a: Number, b: Number) -> float:
        """Divide a by b.

        Args:
            a: First number (dividend)
            b: Second number (divisor)

        Returns:
            The result of a / b

        Raises:
            ZeroDivisionError: If b is 0
        """
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        self.last_result = a / b
        return self.last_result

    def square_root(self, a: Number) -> float:
        """Calculate the square root of a number.

        Args:
            a: The number to calculate the square root of

        Returns:
            The square root of a

        Raises:
            ValueError: If a is negative
        """
        if a < 0:
            raise ValueError("Cannot calculate square root of a negative number")
        self.last_result = math.sqrt(a)
        return self.last_result

    def power(self, a: Number, b: Number) -> Number:
        """Calculate a raised to the power of b.

        Args:
            a: The base
            b: The exponent

        Returns:
            a raised to the power of b
        """
        self.last_result = a ** b
        return self.last_result

    def log(self, a: Number, base: Number = math.e) -> float:
        """Calculate the logarithm of a with the specified base.

        Args:
            a: The number to calculate the logarithm of
            base: The base of the logarithm (default: e)

        Returns:
            The logarithm of a with the specified base

        Raises:
            ValueError: If a is less than or equal to 0, or base is less than or equal to 0 or 1
        """
        if a <= 0:
            raise ValueError("Cannot calculate logarithm of a non-positive number")
        if base <= 0 or base == 1:
            raise ValueError("Invalid logarithm base")

        if base == math.e:
            self.last_result = math.log(a)
        else:
            self.last_result = math.log(a, base)
        return self.last_result

    def get_last_result(self) -> Optional[Number]:
        """Get the result of the last calculation.

        Returns:
            The result of the last calculation or None if no calculation has been performed
        """
        return self.last_result

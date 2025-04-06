"""Calculator module providing a simple addition function."""

from typing import Union

Number = Union[int, float]

class Calculator:
    """A simple calculator focused on addition."""

    def __init__(self) -> None:
        """Initialize the calculator."""
        # No state needed for simple addition
        pass

    def add(self, a: Number, b: Number) -> Number:
        """Add two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            The sum of a and b
        """
        result = a + b
        return result

"""Calculator module providing basic and scientific arithmetic operations."""

import math
from typing import Union, Optional
from pydantic import BaseModel, Field, validator

Number = Union[int, float]


class CalculationInput(BaseModel):
    """Base model for calculation inputs."""
    a: Number = Field(..., description="First number in calculation")
    b: Optional[Number] = Field(None, description="Second number in calculation (optional for some operations)")

    @validator('a')
    def validate_a(cls, v):
        return v

    @validator('b')
    def validate_b(cls, v):
        return v


class AddInput(CalculationInput):
    """Input model for addition."""
    pass


class SubtractInput(CalculationInput):
    """Input model for subtraction."""
    pass


class MultiplyInput(CalculationInput):
    """Input model for multiplication."""
    pass


class DivideInput(CalculationInput):
    """Input model for division."""
    @validator('b')
    def validate_non_zero_divisor(cls, v):
        if v == 0:
            raise ValueError("Cannot divide by zero")
        return v


class SquareRootInput(BaseModel):
    """Input model for square root calculation."""
    a: Number = Field(..., description="Number to calculate square root of")

    @validator('a')
    def validate_non_negative(cls, v):
        if v < 0:
            raise ValueError("Cannot calculate square root of a negative number")
        return v


class PowerInput(CalculationInput):
    """Input model for power calculation."""
    pass


class LogInput(BaseModel):
    """Input model for logarithm calculation."""
    a: Number = Field(..., description="Number to calculate logarithm of")
    base: Number = Field(math.e, description="Logarithm base (default: e)")

    @validator('a')
    def validate_positive_number(cls, v):
        if v <= 0:
            raise ValueError("Cannot calculate logarithm of a non-positive number")
        return v

    @validator('base')
    def validate_valid_base(cls, v):
        if v <= 0 or v == 1:
            raise ValueError("Invalid logarithm base")
        return v


class CalculationResult(BaseModel):
    """Model for calculation results."""
    result: Number = Field(..., description="Result of the calculation")
    operation: str = Field(..., description="Operation performed")


class Calculator:
    """A simple calculator with basic and scientific operations using Pydantic models."""

    def __init__(self) -> None:
        """Initialize the calculator."""
        self.last_result: Optional[CalculationResult] = None

    def add(self, a: Number, b: Number) -> Number:
        """Add two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            The sum of a and b
        """
        # Validate inputs with Pydantic model
        input_data = AddInput(a=a, b=b)
        result = input_data.a + input_data.b
        self.last_result = CalculationResult(result=result, operation="add")
        return result

    def subtract(self, a: Number, b: Number) -> Number:
        """Subtract b from a.

        Args:
            a: First number
            b: Second number

        Returns:
            The result of a - b
        """
        input_data = SubtractInput(a=a, b=b)
        result = input_data.a - input_data.b
        self.last_result = CalculationResult(result=result, operation="subtract")
        return result

    def multiply(self, a: Number, b: Number) -> Number:
        """Multiply two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            The product of a and b
        """
        input_data = MultiplyInput(a=a, b=b)
        result = input_data.a * input_data.b
        self.last_result = CalculationResult(result=result, operation="multiply")
        return result

    def divide(self, a: Number, b: Number) -> float:
        """Divide a by b.

        Args:
            a: First number (dividend)
            b: Second number (divisor)

        Returns:
            The result of a / b

        Raises:
            ValueError: If b is 0
        """
        # DivideInput will validate non-zero divisor
        input_data = DivideInput(a=a, b=b)
        result = input_data.a / input_data.b
        self.last_result = CalculationResult(result=result, operation="divide")
        return result

    def square_root(self, a: Number) -> float:
        """Calculate the square root of a number.

        Args:
            a: The number to calculate the square root of

        Returns:
            The square root of a

        Raises:
            ValueError: If a is negative
        """
        # SquareRootInput will validate non-negative input
        input_data = SquareRootInput(a=a)
        result = math.sqrt(input_data.a)
        self.last_result = CalculationResult(result=result, operation="square_root")
        return result

    def power(self, a: Number, b: Number) -> Number:
        """Calculate a raised to the power of b.

        Args:
            a: The base
            b: The exponent

        Returns:
            a raised to the power of b
        """
        input_data = PowerInput(a=a, b=b)
        result = input_data.a ** input_data.b
        self.last_result = CalculationResult(result=result, operation="power")
        return result

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
        # LogInput will validate positive input and valid base
        input_data = LogInput(a=a, base=base)
        
        if input_data.base == math.e:
            result = math.log(input_data.a)
        else:
            result = math.log(input_data.a, input_data.base)
            
        self.last_result = CalculationResult(result=result, operation="log")
        return result

    def get_last_result(self) -> Optional[CalculationResult]:
        """Get the result of the last calculation.

        Returns:
            The result object of the last calculation or None if no calculation has been performed
        """
        return self.last_result

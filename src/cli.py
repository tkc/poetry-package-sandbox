"""Command-line interface for the Simple Calculator."""

import argparse
import sys
from typing import List, Optional

from .calculator import Calculator


def parse_args(args: Optional[List[str]] = None) -> argparse.Namespace:
    """Parse command-line arguments.

    Args:
        args: Command-line arguments (defaults to sys.argv[1:])

    Returns:
        Parsed arguments
    """
    parser = argparse.ArgumentParser(
        prog="calculate",
        description="Perform basic arithmetic and scientific calculations",
    )

    subparsers = parser.add_subparsers(dest="operation", help="Operation to perform")
    subparsers.required = True

    # Basic operations
    add_parser = subparsers.add_parser("add", help="Add two numbers")
    add_parser.add_argument("a", type=float, help="First number")
    add_parser.add_argument("b", type=float, help="Second number")

    subtract_parser = subparsers.add_parser(
        "subtract", help="Subtract second number from first"
    )
    subtract_parser.add_argument("a", type=float, help="First number")
    subtract_parser.add_argument("b", type=float, help="Second number")

    multiply_parser = subparsers.add_parser("multiply", help="Multiply two numbers")
    multiply_parser.add_argument("a", type=float, help="First number")
    multiply_parser.add_argument("b", type=float, help="Second number")

    divide_parser = subparsers.add_parser(
        "divide", help="Divide first number by second"
    )
    divide_parser.add_argument("a", type=float, help="Dividend")
    divide_parser.add_argument("b", type=float, help="Divisor")

    # Scientific operations
    sqrt_parser = subparsers.add_parser("sqrt", help="Calculate square root")
    sqrt_parser.add_argument("a", type=float, help="Number to find square root of")

    power_parser = subparsers.add_parser("pow", help="Calculate power")
    power_parser.add_argument("a", type=float, help="Base")
    power_parser.add_argument("b", type=float, help="Exponent")

    log_parser = subparsers.add_parser("log", help="Calculate logarithm")
    log_parser.add_argument("a", type=float, help="Number to find logarithm of")
    log_parser.add_argument(
        "base",
        type=float,
        nargs="?",
        default=10,
        help="Logarithm base (default: 10)",
    )

    return parser.parse_args(args)


def main(args: Optional[List[str]] = None) -> None:
    """Main entry point for the CLI.

    Args:
        args: Command-line arguments (defaults to sys.argv[1:])
    """
    parsed_args = parse_args(args)
    calculator = Calculator()

    try:
        if parsed_args.operation == "add":
            result = calculator.add(parsed_args.a, parsed_args.b)
        elif parsed_args.operation == "subtract":
            result = calculator.subtract(parsed_args.a, parsed_args.b)
        elif parsed_args.operation == "multiply":
            result = calculator.multiply(parsed_args.a, parsed_args.b)
        elif parsed_args.operation == "divide":
            result = calculator.divide(parsed_args.a, parsed_args.b)
        elif parsed_args.operation == "sqrt":
            result = calculator.square_root(parsed_args.a)
        elif parsed_args.operation == "pow":
            result = calculator.power(parsed_args.a, parsed_args.b)
        elif parsed_args.operation == "log":
            result = calculator.log(parsed_args.a, parsed_args.base)
        else:
            print(f"Unknown operation: {parsed_args.operation}")  # noqa: T201
            sys.exit(1)

        print(f"Result: {result}")  # noqa: T201

    except Exception as e:
        print(f"Error: {str(e)}")  # noqa: T201
        sys.exit(1)


if __name__ == "__main__":
    main()

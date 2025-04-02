# Python Packaging Sample: Simple Calculator

This repository demonstrates how to create, structure, and publish a modern Python package using Poetry. It serves as a practical example of Python packaging best practices, featuring a simple calculator library with basic and scientific operations.

## Purpose

The goal of this project is to showcase:

- Python package structure and organization
- Using Poetry for dependency management
- Implementing Pydantic for data validation
- Creating command-line interfaces
- Writing tests and documentation
- Packaging and distribution workflows

## Features

- Basic arithmetic operations (addition, subtraction, multiplication, division)
- Scientific operations (square root, power, logarithm)
- Input validation using Pydantic models
- Command line interface for quick calculations
- Comprehensive error handling

## Package Installation

```bash
# From GitHub
pip install git+https://github.com/tkc/poetry-package-sandbox.git

# With a specific version tag
pip install git+https://github.com/tkc/poetry-package-sandbox.git@v0.0.1
```

## Usage Examples

### Basic Usage

```python
from simple_calculator import Calculator
from pydantic import ValidationError

# Create a calculator instance
calc = Calculator()

# Basic arithmetic
try:
    result = calc.add(5, 3)      # returns 8
    print(f"5 + 3 = {result}")
    
    result = calc.divide(10, 2)  # returns 5.0
    print(f"10 / 2 = {result}")
except ValidationError as e:
    print(f"Validation error: {e}")
```

### Using with Error Handling

```python
try:
    # This will raise a validation error due to division by zero
    result = calc.divide(10, 0)
except ValidationError as e:
    print(f"Invalid input: {e.errors()[0]['msg']}")
    
# Access the last calculation result
last_result = calc.get_last_result()
if last_result:
    print(f"Last result: {last_result.result}, Operation: {last_result.operation}")
```

### Command Line Interface

The package provides a command-line interface for quick calculations:

```bash
# Basic operations
calculate add 5 3
calculate subtract 10 4
calculate multiply 2 3
calculate divide 10 2

# Scientific operations
calculate sqrt 16
calculate pow 2 3
calculate log 100 10
```

## Project Structure

```
simple-calculator/
├── simple_calculator/     # Main package
│   ├── __init__.py        # Package initialization
│   ├── calculator.py      # Calculator implementation with Pydantic models
│   └── cli.py             # Command-line interface
├── tests/                 # Test directory
│   ├── test_calculator.py # Calculator tests
│   └── test_cli.py        # CLI tests
├── examples/              # Example usage
├── pyproject.toml         # Poetry configuration and metadata
├── README.md              # Project documentation
└── LICENSE                # MIT License
```

## Development Guide

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/tkc/poetry-package-sandbox.git
cd poetry-package-sandbox

# Install dependencies with Poetry
poetry install

# Activate the virtual environment
poetry shell
```

### Running Tests

```bash
# Run all tests
poetry run pytest

# Run tests with coverage
poetry run pytest --cov=simple_calculator
```

### Code Quality

```bash
# Format code with ruff
poetry run ruff format simple_calculator tests

# Lint code with ruff
poetry run ruff check simple_calculator tests

# Type checking with mypy
poetry run mypy simple_calculator
```

### Building the Package

```bash
# Create distribution packages
poetry build

# Publish to PyPI (if you have access)
poetry publish
```

## Learning Resources

For more information about Python packaging:

- [Python Packaging Authority (PyPA) Documentation](https://packaging.python.org/)
- [Poetry Documentation](https://python-poetry.org/docs/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Package Distribution Specifications](https://packaging.python.org/specifications/)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

# Simple Calculator

A simple calculator package with basic arithmetic operations built using Poetry.

## Features

- Basic arithmetic operations (addition, subtraction, multiplication, division)
- Scientific operations (square root, power, logarithm)
- Command line interface for quick calculations

## Installation

```bash
# From PyPI (when published)
pip install simple-calculator

# From GitHub
pip install git+https://github.com/tkc/poetry-package-sandbox.git
```

## Usage

### As a library

```python
from simple_calculator import Calculator

# Create a calculator instance
calc = Calculator()

# Perform calculations
result1 = calc.add(5, 3)      # 8
result2 = calc.subtract(10, 4)  # 6
result3 = calc.multiply(2, 3)   # 6
result4 = calc.divide(10, 2)    # 5.0

# Scientific operations
result5 = calc.square_root(16)  # 4.0
result6 = calc.power(2, 3)      # 8
result7 = calc.log(100, 10)     # 2.0
```

### From the command line

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

## Development

### Setup

```bash
# Clone the repository
git clone https://github.com/tkc/poetry-package-sandbox.git
cd poetry-package

# Install dependencies
poetry install
```

### Running tests

```bash
poetry run pytest
```

### Code formatting and linting

```bash
# コードのフォーマットとリント（ruffを使用）
poetry run ruff format simple_calculator tests
poetry run ruff check simple_calculator tests

# 全ての問題を自動修正
poetry run ruff check --fix simple_calculator tests

# 型チェック
poetry run mypy simple_calculator
```

## License

MIT

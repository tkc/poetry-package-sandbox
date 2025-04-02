#!/usr/bin/env python3
"""Advanced CLI for the simple calculator."""

import argparse
import sys

from simple_calculator import Calculator


def calculate_compound_interest(principal, rate, time, compounds_per_year=1):
    """
    複利計算を行います。

    Args:
        principal: 元金
        rate: 年利率 (例: 0.05 = 5%)
        time: 期間（年）
        compounds_per_year: 1年あたりの複利計算回数

    Returns:
        最終的な金額
    """
    calc = Calculator()
    rate_per_period = calc.divide(rate, compounds_per_year)
    one_plus_rate = calc.add(1, rate_per_period)
    total_compounds = calc.multiply(compounds_per_year, time)
    compound_factor = calc.power(one_plus_rate, total_compounds)

    return calc.multiply(principal, compound_factor)


def parse_args(args=None):
    parser = argparse.ArgumentParser(
        description="Advanced calculator with scientific operations"
    )

    subparsers = parser.add_subparsers(dest="operation", help="Advanced operations")
    subparsers.required = True

    # 複利計算の定義
    compound_parser = subparsers.add_parser(
        "compound", help="Compound interest calculation"
    )
    compound_parser.add_argument("principal", type=float, help="Principal amount")
    compound_parser.add_argument(
        "rate", type=float, help="Annual interest rate (as decimal)"
    )
    compound_parser.add_argument("time", type=float, help="Time in years")
    compound_parser.add_argument(
        "--compounds", type=int, default=1, help="Compounds per year"
    )

    # ここに他の高度な演算を追加できます
    # 例: quadratic_parser = subparsers.add_parser("quadratic", help="Solve quadratic equation")
    # quadratic_parser.add_argument("a", type=float, help="Coefficient a")
    # ...

    return parser.parse_args(args)


def main(args=None):
    """Main entry point for advanced CLI."""
    parsed_args = parse_args(args)

    try:
        if parsed_args.operation == "compound":
            result = calculate_compound_interest(
                parsed_args.principal,
                parsed_args.rate,
                parsed_args.time,
                parsed_args.compounds,
            )
            print(f"Compound Interest Result: {result:.2f}")  # noqa: T201

        # 他の操作の実装
        # elif parsed_args.operation == "quadratic":
        #     # 二次方程式の解を計算するコード
        #     pass

        else:
            print(  # noqa: T201
                f"Error: Unknown advanced operation '{parsed_args.operation}'",
                file=sys.stderr,
            )
            sys.exit(1)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)  # noqa: T201
        sys.exit(1)


if __name__ == "__main__":
    main()

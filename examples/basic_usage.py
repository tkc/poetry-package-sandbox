#!/usr/bin/env python3
"""
基本的な使用例 - simple-calculatorパッケージの基本機能を示します。
"""

from simple_calculator import Calculator

def main():
    """simple-calculatorの基本的な使用例を示します。"""
    print("===== Simple Calculator - Basic Usage Example =====")

    # Calculatorのインスタンスを作成
    calc = Calculator()

    # 基本的な算術演算
    print("\n--- Basic Arithmetic Operations ---")
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"10 - 4 = {calc.subtract(10, 4)}")
    print(f"6 * 7 = {calc.multiply(6, 7)}")
    print(f"20 / 4 = {calc.divide(20, 4)}")

    # 科学的な演算
    print("\n--- Scientific Operations ---")
    print(f"√16 = {calc.square_root(16)}")
    print(f"2^8 = {calc.power(2, 8)}")
    print(f"log₁₀(1000) = {calc.log(1000, 10)}")
    print(f"ln(e) = {calc.log(calc.power(2.718281828459045, 1))}")

    # 計算履歴
    print("\n--- Last Result ---")
    print(f"Last result: {calc.get_last_result()}")

    # エラー処理の例
    print("\n--- Error Handling Examples ---")
    try:
        result = calc.divide(10, 0)
    except ZeroDivisionError as e:
        print(f"Error caught: {e}")

    try:
        result = calc.square_root(-9)
    except ValueError as e:
        print(f"Error caught: {e}")

    try:
        result = calc.log(-5)
    except ValueError as e:
        print(f"Error caught: {e}")


if __name__ == "__main__":
    main()

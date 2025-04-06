#!/usr/bin/env python3
"""
基本的な使用例 - simple-calculatorパッケージの基本機能を示します。
"""

from calculator import Calculator


def main():
    """simple-calculatorの基本的な使用例を示します。"""
    print("===== Simple Calculator - Basic Usage Example =====")

    # Calculatorのインスタンスを作成
    calc = Calculator()

    # 基本的な算術演算
    print("\n--- Basic Arithmetic Operations ---")
    print(f"5 + 3 = {calc.add(5, 3)}")



if __name__ == "__main__":
    main()

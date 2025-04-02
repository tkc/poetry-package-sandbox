#!/usr/bin/env python3
"""
高度な使用例 - simple-calculatorパッケージを使った少し複雑な計算例を示します。
"""

import math
from simple_calculator import Calculator

def compound_interest(principal: float, rate: float, time: float, compounds_per_year: int = 1) -> float:
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
    
    # A = P(1 + r/n)^(nt)
    rate_per_period = calc.divide(rate, compounds_per_year)
    one_plus_rate = calc.add(1, rate_per_period)
    total_compounds = calc.multiply(compounds_per_year, time)
    compound_factor = calc.power(one_plus_rate, total_compounds)
    
    return calc.multiply(principal, compound_factor)


def quadratic_formula(a: float, b: float, c: float) -> tuple:
    """
    二次方程式 ax² + bx + c = 0 の解を求めます。
    
    Args:
        a: x²の係数
        b: xの係数
        c: 定数項
        
    Returns:
        解のタプル (x1, x2) または虚数解の場合は None
    """
    calc = Calculator()
    
    # 判別式を計算
    discriminant = calc.subtract(
        calc.power(b, 2),
        calc.multiply(4, calc.multiply(a, c))
    )
    
    # 判別式が0未満の場合は実数解なし
    if discriminant < 0:
        return None
    
    # 解の公式: x = (-b ± √(b² - 4ac)) / 2a
    sqrt_discriminant = calc.square_root(discriminant)
    
    denominator = calc.multiply(2, a)
    
    x1 = calc.divide(
        calc.subtract(calc.multiply(b, -1), sqrt_discriminant),
        denominator
    )
    
    x2 = calc.divide(
        calc.add(calc.multiply(b, -1), sqrt_discriminant),
        denominator
    )
    
    return (x1, x2)


def main():
    """simple-calculatorの高度な使用例を示します。"""
    print("===== Simple Calculator - Advanced Usage Example =====")
    
    # 複利計算の例
    print("\n--- Compound Interest Example ---")
    principal = 1000  # 元金1000ドル
    rate = 0.05       # 年利5%
    time = 10         # 10年間
    
    # 異なる複利計算頻度での計算
    annual = compound_interest(principal, rate, time, 1)
    semiannual = compound_interest(principal, rate, time, 2)
    quarterly = compound_interest(principal, rate, time, 4)
    monthly = compound_interest(principal, rate, time, 12)
    daily = compound_interest(principal, rate, time, 365)
    
    print(f"Principal: ${principal:.2f}")
    print(f"Annual Rate: {rate*100:.1f}%")
    print(f"Time: {time} years")
    print(f"Annual compounding: ${annual:.2f}")
    print(f"Semi-annual compounding: ${semiannual:.2f}")
    print(f"Quarterly compounding: ${quarterly:.2f}")
    print(f"Monthly compounding: ${monthly:.2f}")
    print(f"Daily compounding: ${daily:.2f}")
    
    # 二次方程式を解く例
    print("\n--- Quadratic Equation Solver Example ---")
    
    # 例1: x² - 5x + 6 = 0 (解: x = 2, x = 3)
    a1, b1, c1 = 1, -5, 6
    roots1 = quadratic_formula(a1, b1, c1)
    print(f"Equation: {a1}x² + ({b1})x + {c1} = 0")
    print(f"Roots: x = {roots1[0]}, x = {roots1[1]}")
    
    # 例2: 2x² - 4x - 6 = 0
    a2, b2, c2 = 2, -4, -6
    roots2 = quadratic_formula(a2, b2, c2)
    print(f"Equation: {a2}x² + ({b2})x + {c2} = 0")
    print(f"Roots: x = {roots2[0]}, x = {roots2[1]}")
    
    # 例3: x² + x + 1 = 0 (実数解なし)
    a3, b3, c3 = 1, 1, 1
    roots3 = quadratic_formula(a3, b3, c3)
    print(f"Equation: {a3}x² + {b3}x + {c3} = 0")
    print(f"Roots: {roots3} (No real solutions)")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
高度な計算機能のAPI使用例 - 高度な計算機能を直接Pythonコードから利用する方法を示します。
"""

from simple_calculator import Calculator
try:
    # 注意: このインポートはsimple_calculatorパッケージに
    # advanced_cliモジュールが実装されている場合にのみ動作します
    from simple_calculator.advanced_cli import calculate_compound_interest
    HAS_ADVANCED_FEATURES = True
except ImportError:
    HAS_ADVANCED_FEATURES = False
    print("注意: advanced_cliモジュールが見つかりません。基本的な計算機能のみ使用します。")


class AdvancedCalculations:
    """高度な計算機能を提供するクラス"""
    
    def __init__(self):
        """基本計算機クラスのインスタンスを初期化"""
        self.calc = Calculator()
    
    def compound_interest(self, principal, rate, time, compounds_per_year=1):
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
        # advanced_cliが利用可能ならそれを使う
        if HAS_ADVANCED_FEATURES:
            # advanced_cliモジュールの関数を直接呼び出す
            # 注意: この関数がadvanced_cli.pyに存在する必要があります
            try:
                return calculate_compound_interest(principal, rate, time, compounds_per_year)
            except NameError:
                print("警告: calculate_compound_interest関数がadvanced_cliに見つかりません。手動で計算します。")
                # フォールバック実装へ
        
        # 利用できない場合や関数が見つからない場合は自分で実装
        rate_per_period = self.calc.divide(rate, compounds_per_year)
        one_plus_rate = self.calc.add(1, rate_per_period)
        total_compounds = self.calc.multiply(compounds_per_year, time)
        compound_factor = self.calc.power(one_plus_rate, total_compounds)
        
        return self.calc.multiply(principal, compound_factor)
    
    def quadratic_formula(self, a, b, c):
        """
        二次方程式 ax² + bx + c = 0 の解を求めます。
        
        Args:
            a: x²の係数
            b: xの係数
            c: 定数項
            
        Returns:
            解のタプル (x1, x2) または判別式が負の場合はNone
        """
        # 判別式を計算
        discriminant = self.calc.subtract(
            self.calc.power(b, 2),
            self.calc.multiply(4, self.calc.multiply(a, c))
        )
        
        # 判別式が0未満の場合は実数解なし
        if discriminant < 0:
            return None
        
        # 解の公式: x = (-b ± √(b² - 4ac)) / 2a
        sqrt_discriminant = self.calc.square_root(discriminant)
        
        denominator = self.calc.multiply(2, a)
        
        # ゼロ除算を避ける
        if denominator == 0:
            raise ValueError("Coefficient 'a' cannot be zero for quadratic formula")

        x1 = self.calc.divide(
            self.calc.subtract(self.calc.multiply(b, -1), sqrt_discriminant),
            denominator
        )
        
        x2 = self.calc.divide(
            self.calc.add(self.calc.multiply(b, -1), sqrt_discriminant),
            denominator
        )
        
        return (x1, x2)
    
    def fibonacci(self, n):
        """
        フィボナッチ数列のn番目の数を計算します。
        
        Args:
            n: 計算する項の番号（0から開始）
            
        Returns:
            n番目のフィボナッチ数
        """
        if not isinstance(n, int) or n < 0:
             raise ValueError("Input must be a non-negative integer")
        if n <= 0:
            return 0
        if n == 1:
            return 1
            
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, self.calc.add(a, b)
        
        return b
    
    def factorial(self, n):
        """
        階乗n!を計算します。
        
        Args:
            n: 階乗を計算する非負整数
            
        Returns:
            n!の値
        """
        if not isinstance(n, int) or n < 0:
            raise ValueError("Cannot calculate factorial of negative number or non-integer")
        
        if n <= 1:
            return 1
            
        result = 1
        for i in range(2, n + 1):
            result = self.calc.multiply(result, i)
            
        return result


def main():
    """高度な計算機能の使用例を示します"""
    print("===== Simple Calculator - Advanced API Usage =====")
    
    # 高度な計算クラスをインスタンス化
    adv_calc = AdvancedCalculations()
    
    # 複利計算の例
    print("\n--- 複利計算の例 ---")
    principal = 1000    # 元金1000ドル
    rate = 0.05         # 年利5%
    time = 10           # 10年間
    
    # 異なる複利計算頻度での計算
    try:
        annual = adv_calc.compound_interest(principal, rate, time, 1)
        semiannual = adv_calc.compound_interest(principal, rate, time, 2)
        quarterly = adv_calc.compound_interest(principal, rate, time, 4)
        monthly = adv_calc.compound_interest(principal, rate, time, 12)
        daily = adv_calc.compound_interest(principal, rate, time, 365)
        
        print(f"元金: ${principal:.2f}")
        print(f"年利: {rate*100:.1f}%")
        print(f"期間: {time}年")
        print(f"年1回の複利計算: ${annual:.2f}")
        print(f"年2回の複利計算: ${semiannual:.2f}")
        print(f"年4回の複利計算: ${quarterly:.2f}")
        print(f"毎月の複利計算: ${monthly:.2f}")
        print(f"毎日の複利計算: ${daily:.2f}")
    except Exception as e:
        print(f"複利計算中にエラーが発生しました: {e}")

    # 二次方程式を解く例
    print("\n--- 二次方程式を解く例 ---")
    
    # 例1: x² - 5x + 6 = 0 (解: x = 2, x = 3)
    a1, b1, c1 = 1, -5, 6
    try:
        roots1 = adv_calc.quadratic_formula(a1, b1, c1)
        if roots1:
            print(f"方程式: {a1}x² + ({b1})x + {c1} = 0")
            print(f"解: x = {roots1[0]}, x = {roots1[1]}")
        else:
            print(f"方程式: {a1}x² + ({b1})x + {c1} = 0 には実数解がありません。")
    except Exception as e:
        print(f"二次方程式1の計算中にエラーが発生しました: {e}")

    # 例2: 2x² - 4x - 6 = 0 (解: x = 3, x = -1)
    a2, b2, c2 = 2, -4, -6
    try:
        roots2 = adv_calc.quadratic_formula(a2, b2, c2)
        if roots2:
            print(f"方程式: {a2}x² + ({b2})x + {c2} = 0")
            # 解の順序が異なる場合があるため、ソートして表示
            sorted_roots = sorted(roots2)
            print(f"解: x = {sorted_roots[0]}, x = {sorted_roots[1]}")
        else:
             print(f"方程式: {a2}x² + ({b2})x + {c2} = 0 には実数解がありません。")
    except Exception as e:
        print(f"二次方程式2の計算中にエラーが発生しました: {e}")

    # 例3: x² + 1 = 0 (実数解なし)
    a3, b3, c3 = 1, 0, 1
    try:
        roots3 = adv_calc.quadratic_formula(a3, b3, c3)
        if roots3:
            print(f"方程式: {a3}x² + {c3} = 0")
            print(f"解: x = {roots3[0]}, x = {roots3[1]}")
        else:
            print(f"方程式: {a3}x² + {c3} = 0 には実数解がありません。")
    except Exception as e:
        print(f"二次方程式3の計算中にエラーが発生しました: {e}")

    # フィボナッチ数列の例
    print("\n--- フィボナッチ数列の例 ---")
    try:
        for i in range(10):
            fib = adv_calc.fibonacci(i)
            print(f"フィボナッチ({i}) = {fib}")
    except Exception as e:
        print(f"フィボナッチ数列の計算中にエラーが発生しました: {e}")
    
    # 階乗計算の例
    print("\n--- 階乗計算の例 ---")
    try:
        for i in range(6):
            fact = adv_calc.factorial(i)
            print(f"{i}! = {fact}")
        # エラーケース
        # print(f"(-1)! = {adv_calc.factorial(-1)}") 
    except ValueError as e:
         print(f"階乗計算エラー: {e}")
    except Exception as e:
        print(f"階乗計算中に予期せぬエラーが発生しました: {e}")

    print("\nすべての例が完了しました。")

if __name__ == "__main__":
    main()

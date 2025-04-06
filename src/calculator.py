"""
Calculator package - エイリアスモジュール
内部実装は cal モジュールですが、calculator としてインポートできるようにします
"""

from .cal import *

# パッケージからエクスポートする全てのシンボルをここに列挙
__all__ = ['Calculator', 'calculate_compound_interest']

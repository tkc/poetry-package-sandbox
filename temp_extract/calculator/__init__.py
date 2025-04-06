"""
Calculator package - パッケージレベルのエイリアスモジュール
内部実装は cal モジュールですが、calculator パッケージとしてインポートできるようにします
"""

import cal
from cal import Calculator

# パッケージからエクスポートする全てのシンボルをここに列挙
__all__ = ['Calculator']

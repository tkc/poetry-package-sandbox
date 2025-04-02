# Simple Calculator - 使用例

このディレクトリには、`simple-calculator`パッケージを使用した様々なサンプルコードが含まれています。このディレクトリ自体も Poetry プロジェクトとなっており、親パッケージを依存関係として利用します。

## 実行方法

以下のコマンドでこのディレクトリの例を実行できます：

```bash
# examplesディレクトリに移動
cd examples

# Poetryの仮想環境を構築しパッケージをインストール（最初に一度だけ必要）
poetry install

# 基本的な使用例
poetry run python basic_usage.py

# コードのフォーマットとリント
poetry run ruff format .
poetry run ruff check .
```

## パッケージのインストール方法

GitHub から直接インストールする場合は、以下のように指定します：

```toml
[tool.poetry.dependencies]
python = "^3.8"
simple-calculator = {git = "https://github.com/tkc/poetry-package-sandbox.git"}
```

## 例の説明

### 1. basic_usage.py

`simple-calculator`パッケージの基本的な機能を紹介するシンプルな例です。以下を含みます：

- 基本的な算術演算（加算、減算、乗算、除算）
- 科学的な演算（平方根、べき乗、対数）
- 最後の結果の取得
- 基本的なエラー処理

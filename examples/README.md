# Simple Calculator - 使用例コレクション

このディレクトリは、`simple-calculator`パッケージの実践的な使用例を提供する学習リソースです。Poetryを使ったPythonパッケージの効果的な利用方法と、プロジェクトにどのように組み込むかを示しています。

## このディレクトリの目的

このexamplesディレクトリは以下の点を実演しています：

- 外部パッケージとしてsimple-calculatorを利用する方法
- 依存関係としてGitリポジトリから直接パッケージをインストールする方法
- Poetryを使った独立した開発環境の構築と管理
- パッケージのさまざまな機能とエラー処理パターンの展示
- Pydanticを活用した入力検証の実例

## セットアップ方法

このexamplesプロジェクトは独立したPoetryプロジェクトとなっており、メインのsimple-calculatorパッケージを依存関係として利用します：

```bash
# examplesディレクトリに移動
cd examples

# Poetryの仮想環境を構築し依存関係をインストール
poetry install --no-root

# 例を実行
poetry run python basic_usage.py
```

## パッケージの参照方法

このプロジェクトでは、GitHubリポジトリから直接パッケージを参照しています：

```toml
# examples/pyproject.tomlの設定
[tool.poetry.dependencies]
python = "^3.8"
simple-calculator = {git = "https://github.com/tkc/poetry-package-sandbox.git"}

# 特定のバージョンを参照する場合
# simple-calculator = {git = "https://github.com/tkc/poetry-package-sandbox.git", tag = "v0.0.1"}

# 特定のコミットを参照する場合
# simple-calculator = {git = "https://github.com/tkc/poetry-package-sandbox.git", rev = "コミットハッシュ"}
```

これにより、パッケージが公式に公開されていなくても、GitHubから直接インストールして利用できることを示しています。

## 使用例の説明

### 1. basic_usage.py

`simple-calculator`パッケージの基本的な機能を紹介するシンプルな例です。以下を含みます：

- 基本的な算術演算（加算、減算、乗算、除算）
- 科学的な演算（平方根、べき乗、対数）
- 最後の結果の取得
- 基本的なエラー処理

### 2. advanced_api_usage.py

高度な計算機能をプログラムに組み込む例を示しています：

- 複利計算の実装と異なる複利計算頻度の比較
- 二次方程式の解法
- フィボナッチ数列計算
- 階乗計算

これは単純な計算機能を組み合わせてより高度な機能を実装する方法を示しています。

## コード品質の維持

このプロジェクトでは、ruffを使用してコードの品質を維持しています：

```bash
# コードのフォーマット
poetry run ruff format .

# コードのリント
poetry run ruff check .
```

## 応用例の作成

独自の応用例を追加することで、simple-calculatorパッケージのさまざまな使い方を探求できます。新しい例を作成する際は：

1. Pythonファイルを作成（例: `advanced_example.py`）
2. パッケージをインポートして必要な機能を実装
3. 適切なエラー処理を組み込む
4. コメントで処理内容を説明

## 学習のヒント

- 各サンプルコードの実装を詳しく見て、Calculatorクラスの使い方を理解しましょう
- Pydanticの検証エラーがどのように発生し、処理されるかに注目してください
- パッケージをさまざまな文脈で使用する方法を考えてみましょう
- pyproject.tomlの設定を変更して、異なる参照方法を試してみてください

このexamplesディレクトリを通じて、モダンなPythonパッケージの効果的な利用方法を学ぶことができます。

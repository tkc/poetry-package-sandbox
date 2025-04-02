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

# 高度な使用例
poetry run python advanced_usage.py

# バッチ処理の例
poetry run python batch_processing.py

# CLIの例（シェルスクリプト）
poetry run bash cli_examples.sh

# コードのフォーマットとリント
poetry run ruff format .
poetry run ruff check .
```

## パッケージのインストール方法

親ディレクトリのパッケージは、ローカルのパスから依存関係として参照されます：

```toml
# examples/pyproject.toml内の設定
[tool.poetry.dependencies]
python = "^3.8"
simple-calculator = {path = ".."}
```

GitHubから直接インストールする場合は、以下のように指定します：

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

### 2. advanced_usage.py

より複雑な計算を行うためにパッケージを使用する方法を示します：

- 複利計算の実装と様々な複利計算頻度の比較
- 二次方程式を解く方法の実装

### 3. batch_processing.py

CSVファイルを処理する実用的な例です：

- CSVデータの読み込みと書き込み
- 売上データの処理と税金計算
- 計算結果を含む新しいCSVファイルの生成

### 4. cli_examples.sh

コマンドラインインターフェース（CLI）の使用方法を示すシェルスクリプトです：

- 基本的なコマンドの使用方法
- ヘルプの表示方法
- エラー処理のデモンストレーション

## 応用例

これらの例を拡張して、独自のプロジェクトに役立てることができます：

- 財務計算アプリケーション
- データ処理パイプライン
- 科学的計算ツール
- カスタムCLIツール

詳細は各スクリプトのコメントを参照してください。

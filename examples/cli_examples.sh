#!/bin/bash
# simple-calculatorパッケージのCLIの使用例

# examplesディレクトリ内で実行する前提
cd "$(dirname "$0")"

echo "===== Simple Calculator - CLI Examples ====="
echo ""

echo "# 基本的な算術演算"
echo "$ calculate add 10 5"
poetry run calculate add 10 5

echo -e "\n$ calculate subtract 10 5"
poetry run calculate subtract 10 5

echo -e "\n$ calculate multiply 10 5"
poetry run calculate multiply 10 5

echo -e "\n$ calculate divide 10 5"
poetry run calculate divide 10 5

echo -e "\n# 科学的な演算"
echo "$ calculate sqrt 16"
poetry run calculate sqrt 16

echo -e "\n$ calculate pow 2 8"
poetry run calculate pow 2 8

echo -e "\n$ calculate log 100 10"
poetry run calculate log 100 10

echo -e "\n# エラー処理の例"
echo "$ calculate divide 10 0"
poetry run calculate divide 10 0 || echo "エラーが発生しました（これは正常な動作です）"

echo -e "\n# ヘルプの表示"
echo "$ calculate --help"
poetry run calculate --help

echo -e "\n$ calculate add --help"
poetry run calculate add --help

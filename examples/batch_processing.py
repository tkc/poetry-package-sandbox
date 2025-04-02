#!/usr/bin/env python3
"""
バッチ処理の例 - CSVファイルのデータ処理にsimple-calculatorを使用する例を示します。
"""

import csv
import os
from typing import List, Dict, Any
from simple_calculator import Calculator


def read_csv(filename: str) -> List[Dict[str, str]]:
    """
    CSVファイルを読み込み、dictのリストとして返します。
    
    Args:
        filename: 読み込むCSVファイルのパス
        
    Returns:
        各行がdictで表現されたリスト
    """
    data = []
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data


def write_csv(filename: str, data: List[Dict[str, Any]], fieldnames: List[str]) -> None:
    """
    dictのリストをCSVファイルに書き込みます。
    
    Args:
        filename: 書き込むCSVファイルのパス
        data: 書き込むデータ（dictのリスト）
        fieldnames: CSVのヘッダー
    """
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def process_sales_data(input_file: str, output_file: str) -> None:
    """
    売上データを処理し、合計、税金、最終金額を計算します。
    
    Args:
        input_file: 入力CSVファイルのパス
        output_file: 出力CSVファイルのパス
    """
    # CSVファイルを読み込む
    data = read_csv(input_file)
    
    calc = Calculator()
    tax_rate = 0.1  # 10%の税率
    
    # 各行に計算結果を追加
    for row in data:
        # 数値として処理
        quantity = float(row['quantity'])
        price = float(row['price'])
        
        # 小計を計算
        subtotal = calc.multiply(quantity, price)
        
        # 税金を計算
        tax = calc.multiply(subtotal, tax_rate)
        
        # 合計を計算
        total = calc.add(subtotal, tax)
        
        # 結果を行に追加
        row['subtotal'] = f"{subtotal:.2f}"
        row['tax'] = f"{tax:.2f}"
        row['total'] = f"{total:.2f}"
    
    # 新しいフィールド名を追加
    fieldnames = ['product_id', 'product_name', 'quantity', 'price', 'subtotal', 'tax', 'total']
    
    # 結果をCSVファイルに書き込む
    write_csv(output_file, data, fieldnames)
    
    print(f"Processed {len(data)} sales records")
    print(f"Output written to {output_file}")


def main():
    """売上データを処理する例を示します。"""
    print("===== Simple Calculator - Batch Processing Example =====")
    
    # 作業ディレクトリを例のディレクトリに設定
    examples_dir = os.path.dirname(os.path.abspath(__file__))
    
    # サンプルデータを作成
    sample_data = [
        {'product_id': '001', 'product_name': 'Laptop', 'quantity': '2', 'price': '1200.00'},
        {'product_id': '002', 'product_name': 'Mouse', 'quantity': '5', 'price': '25.50'},
        {'product_id': '003', 'product_name': 'Keyboard', 'quantity': '3', 'price': '85.99'},
        {'product_id': '004', 'product_name': 'Monitor', 'quantity': '2', 'price': '350.00'},
        {'product_id': '005', 'product_name': 'Headphones', 'quantity': '4', 'price': '175.00'}
    ]
    
    # 入出力ファイルのパス
    input_file = os.path.join(examples_dir, 'sales_data.csv')
    output_file = os.path.join(examples_dir, 'sales_data_processed.csv')
    
    # サンプルデータをCSVファイルに書き込む
    fieldnames = ['product_id', 'product_name', 'quantity', 'price']
    write_csv(input_file, sample_data, fieldnames)
    print(f"Sample data written to {input_file}")
    
    # データを処理
    process_sales_data(input_file, output_file)
    
    # 結果を表示
    print("\n--- First 3 rows of processed data ---")
    processed_data = read_csv(output_file)
    for i, row in enumerate(processed_data):
        if i >= 3:
            break
        print(f"Product: {row['product_name']}, Quantity: {row['quantity']}, Price: ${row['price']}")
        print(f"Subtotal: ${row['subtotal']}, Tax: ${row['tax']}, Total: ${row['total']}")
        print()


if __name__ == "__main__":
    main()

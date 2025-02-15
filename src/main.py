from first import First

def main():
    # Firstクラスの使用例
    first = First("こんにちは")
    print(f"初期テキスト: {first.get_text()}")
    
    # テキストの追加
    first.append_text("、世界！")
    print(f"テキスト追加後: {first.get_text()}")
    
    # テキストの設定
    first.set_text("新しいテキスト")
    print(f"テキスト変更後: {first.get_text()}")

if __name__ == "__main__":
    main()

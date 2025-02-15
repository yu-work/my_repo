# First Class

シンプルなテキスト処理クラスの実装例です。

## 機能
- テキストの保存と取得
- テキストの追加
- テキストの設定

## 使用例
```python
# インスタンスの作成
first = First("こんにちは")

# テキストの取得
text = first.get_text()  # "こんにちは"

# テキストの追加
first.append_text("、世界！")  # "こんにちは、世界！"

# テキストの設定
first.set_text("新しいテキスト")
```

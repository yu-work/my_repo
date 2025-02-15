class Person:
    """人物を表現するクラス"""
    
    # クラス変数としてサンプルの性格データを定義
    personality_data = {
        "田中": "明るく社交的",
        "鈴木": "冷静で論理的",
        "佐藤": "優しく思いやりがある",
        "山田": "情熱的で積極的",
        "中村": "慎重で計画的"
    }
    
    def __init__(self, name: str, age: int):
        """
        人物の初期化
        
        Args:
            name (str): 名前
            age (int): 年齢
        """
        self.name = name
        self.age = age
        self.personality = self.personality_data.get(name, "性格情報なし")
    
    def greet(self) -> str:
        """
        挨拶を返す
        
        Returns:
            str: 挨拶メッセージ
        """
        return f"こんにちは、{self.name}です。{self.age}歳です。私は{self.personality}な性格です。"
    
    def have_birthday(self) -> None:
        """誕生日を迎えて年齢を1つ増やす"""
        self.age += 1
    
    @classmethod
    def get_all_personalities(cls) -> dict:
        """
        全ての性格データを取得
        
        Returns:
            dict: 名前と性格の対応辞書
        """
        return cls.personality_data.copy()

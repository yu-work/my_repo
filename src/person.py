class Person:
    """人物を表現するクラス"""
    
    def __init__(self, name: str, age: int):
        """
        人物の初期化
        
        Args:
            name (str): 名前
            age (int): 年齢
        """
        self.name = name
        self.age = age
    
    def greet(self) -> str:
        """
        挨拶を返す
        
        Returns:
            str: 挨拶メッセージ
        """
        return f"こんにちは、{self.name}です。{self.age}歳です。"
    
    def have_birthday(self) -> None:
        """誕生日を迎えて年齢を1つ増やす"""
        self.age += 1

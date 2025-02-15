class First:
    """最初のクラス実装"""
    
    def __init__(self, text: str = ""):
        """
        Firstクラスの初期化
        
        Args:
            text (str): 初期テキスト
        """
        self.text = text
    
    def set_text(self, text: str) -> None:
        """
        テキストを設定する
        
        Args:
            text (str): 設定するテキスト
        """
        self.text = text
    
    def get_text(self) -> str:
        """
        現在のテキストを取得する
        
        Returns:
            str: 保存されているテキスト
        """
        return self.text
    
    def append_text(self, additional_text: str) -> None:
        """
        既存のテキストに新しいテキストを追加する
        
        Args:
            additional_text (str): 追加するテキスト
        """
        self.text += additional_text

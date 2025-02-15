from person import Person

def main():
    # 全ての性格データを表示
    print("登録されている性格データ:")
    personalities = Person.get_all_personalities()
    for name, personality in personalities.items():
        print(f"{name}: {personality}")
    
    print("\n=== 人物の例 ===")
    
    # 登録されている人物の例
    person1 = Person("田中", 25)
    print(person1.greet())
    
    # 登録されていない人物の例
    person2 = Person("木村", 30)
    print(person2.greet())
    
    # 誕生日のテスト
    person1.have_birthday()
    print(f"\n{person1.name}さんが誕生日を迎えました！")
    print(f"新しい年齢: {person1.age}歳")

if __name__ == "__main__":
    main()

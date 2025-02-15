from person import Person

def main():
    # Personクラスの使用例
    person = Person("田中", 25)
    print(person.greet())  # 挨拶を出力
    
    person.have_birthday()  # 誕生日
    print(f"誕生日を迎えました！新しい年齢: {person.age}")

if __name__ == "__main__":
    main()

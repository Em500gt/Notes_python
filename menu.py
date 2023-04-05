import csv

class menu():
    
    def get_menu():
        while True:
            
            print("\n1 - Просмотр заметок\n2 - Добавление заметок\n3 - Редактирование заметок\n4 - Удаление заметок\n0 - Выход\n")
            
            try:
                n = int(input("Выберите операцию: "))
                if n > 4 or n < 0:
                    print("Такой операции не существует!")
            except ValueError:
                print("Такой операции не существует!")
                break

    def add_notes():
        pass
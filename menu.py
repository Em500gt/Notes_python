import csv
import database

class menu():
    
    def get_menu():
        while True:
            
            print("\n1 - Просмотр заметок\n2 - Добавление заметок\n3 - Редактирование заметок\n4 - Удаление заметок\n0 - Выход\n")
            
            try:
                n = int(input("Выберите операцию: "))
            except ValueError:
                print("\nТакой операции не существует!")
                continue

            if n > 4 or n < 0:
                print("\nТакой операции не существует!")
            
            elif n == 0:
                break

            elif n == 1:
                database.show_record()

            elif n == 2:
                database.record(input("\nВведите заголовок заметки: "), input("Введите тело заметки: "))
            
            elif n == 3:
                database.editing_records(input("Введите заголовок заметки: "))

            elif n == 4:
                database.delete_records(input("Введите заголовок заметки: "))
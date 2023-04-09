from datetime import *
import os.path
import csv
import copy

db = list()
file_name_db = ''

def db_init(name='base.csv'):
    global db
    global file_name_db
    file_name_db = name

    if os.path.exists(file_name_db):

        with open(file_name_db, 'r', newline='') as csv_file:
            reader = csv.reader(csv_file)

            for i in reader:
                if i[0] != 'ID':
                    db.append(i)
    else:
        open(file_name_db, 'w', newline='').close()

def record(header, text):

    users = [header.title(), text.title(), datetime.now(tz=None)]
    db.append(users)

    with open(file_name_db, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(users)
    
    print("\nЗаметка успешно добавлена")

def delete_records(id):
    global db
    global file_name_db

    for i in db:
        if i[0] == id:
            print(f'\nВы хотите удалить эту запись?')
            print(f"\nЗаголовок заметки -> {i[0]}")
            print(f"Тело заметки -> {i[1]}")
            print(f"Дата последнего изменения -> {i[2]}\n")
            n = input("Да - (y), Нет - (n): ")
            if n == 'y':
                db.remove(i)
                break

    with open(file_name_db, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='\'', quoting=csv.QUOTE_MINIMAL)

        for i in db:
            writer.writerow(i)
            

def show_record():
    for i in db:
        print(f"\nЗаголовок заметки -> {i[0]}")
        print(f"Тело заметки -> {i[1]}")
        print(f"Дата последнего изменения -> {i[2]}\n")

def show(id):
        for i in db:
            if i[0] == id:
                print(f"\nЗаголовок заметки -> {i[0]}")
                print(f"Тело заметки -> {i[1]}")
                print(f"Дата последнего изменения -> {i[2]}\n")

def editing_records(id):
    global db
    global file_name_db

    for i in db:
        if i[0] == id:
            print(f'\nВы хотите редактировать эту запись?')
            print(f"\nЗаголовок заметки -> {i[0]}")
            print(f"Тело заметки -> {i[1]}")
            print(f"Дата последнего изменения -> {i[2]}\n")
            n = input("Да - (y), Нет - (n): ")
            if n == 'y':
                db.remove(i)
                users = [id.title(), input("Введите тело заметки: ").title(), datetime.now(tz=None)]
                db.append(users)
                break

    with open(file_name_db, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='\'', quoting=csv.QUOTE_MINIMAL)

        for i in db:
            writer.writerow(i)
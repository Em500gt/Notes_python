import csv
import os

class Database():
    db = list()
    global_id = 0
    file_name_db = ''

    def db_init(name='base.csv'):
        global db
        global global_id
        global file_name_db
        file_name_db = name

        if os.path.exists(file_name_db):

            with open(file_name_db, 'r', newline='') as csv_file:
                reader = csv.reader(csv_file)

                for i in reader:
                    if i[0] != 'ID':
                        db.append(i)

                        if int(i[0]) > global_id:
                            global_id = int(i[0])
        else:
            open(file_name_db, 'w', newline='').close()
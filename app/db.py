import sqlite3


# try:
#     students_data = [('Vladislav', 'Levkovich', 21), ('Ivan', 'Ivanov', 19)]
#     connection = sqlite3.connect('test_db.db')
#     cursor = connection.cursor()
#     cursor.execute('''CREATE TABLE IF NOT EXISTS students (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         first_name TEXT NOT NULL,
#         last_name TEXT NOT NULL,
#         age INTEGER
#     )''')
#     # insert_data = cursor.execute("INSERT INTO students (first_name, last_name, age) VALUES (?,?,?)", ('Vlad', 'Levkovich', 21))
#     # insert_data = cursor.executemany("INSERT INTO students (first_name, last_name, age) VALUES (?,?,?)", students_data)
#     select_query = cursor.execute("SELECT * from students")
#     for student in select_query:
#         print('id:', student[0])
#         print('first_name:', student[1])
#         print('last_name:', student[2])
#         print('age:', student[3])
#     # print(select_query)
#     connection.commit()
#     connection.close()
# except sqlite3.Error as e:
#     print(e)


def connect_db():
    # підключаємося до бд
    connection = sqlite3.connect('test_db.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            age INTEGER
        )''')
    return cursor, connection

def get_all_students():
    # отримуємо всі записи
    cursor, _ = connect_db()
    students = cursor.execute("SELECT * from students WHERE age < 20")
    return students

def add_student(first_name, last_name, age):
    # додаємо нового студента
    cursor, connection = connect_db()
    cursor.execute("INSERT INTO students (first_name, last_name, age) VALUES (?,?,?)", (first_name, last_name, age))
    connection.commit()
    return None


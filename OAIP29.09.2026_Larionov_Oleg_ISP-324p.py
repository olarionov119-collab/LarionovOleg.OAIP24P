import sqlite3

DB_NAME = "students.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def create_table(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            group_name TEXT NOT NULL,
            grade INTEGER NOT NULL,
            age INTEGER
        )
    """)
    conn.commit()


def fill_initial_data(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM students")
    count = cursor.fetchone()[0]
    if count == 0:
        students = [
            ("Иванов Иван", "ИСП-101", 5, 18),
            ("Петров Пётр", "ИСП-101", 4, 19),
            ("Сидоров Алексей", "ИСП-102", 3, 20),
            ("Смирнова Анна", "ИСП-102", 5, 18),
            ("Кузнецов Максим", "ИСП-101", 4, 21),
        ]
        cursor.executemany(
            "INSERT INTO students (name, group_name, grade, age) VALUES (?, ?, ?, ?)",
            students,
        )
        conn.commit()
        print("Добавлены стартовые записи (5 студентов).")


def print_students(rows):
    if not rows:
        print("Записи не найдены.")
        return
    print("-" * 70)
    print(f"{'ID':<5}{'ФИО':<25}{'Группа':<12}{'Оценка':<8}{'Возраст':<8}")
    print("-" * 70)
    for row in rows:
        print(f"{row[0]:<5}{row[1]:<25}{row[2]:<12}{row[3]:<8}{row[4]:<8}")
    print("-" * 70)


def show_all(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, group_name, grade, age FROM students")
    print_students(cursor.fetchall())


def add_student(conn):
    name = input("Введите ФИО студента: ").strip()
    if not name:
        print("ФИО не может быть пустым.")
        return
    group_name = input("Введите название группы: ").strip()
    if not group_name:
        print("Группа не может быть пустой.")
        return

    grade = read_int("Введите оценку (2-5): ", 2, 5)
    if grade is None:
        return
    age = read_int("Введите возраст (14-100): ", 14, 100)
    if age is None:
        return

    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (name, group_name, grade, age) VALUES (?, ?, ?, ?)",
        (name, group_name, grade, age),
    )
    conn.commit()
    print(f"Студент «{name}» добавлен. ID = {cursor.lastrowid}")


def find_by_group(conn):
    group_name = input("Введите название группы: ").strip()
    if not group_name:
        print("Группа не может быть пустой.")
        return
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, name, group_name, grade, age FROM students WHERE group_name = ?",
        (group_name,),
    )
    print_students(cursor.fetchall())


def find_by_grade(conn):
    grade = read_int("Введите оценку (2-5): ", 2, 5)
    if grade is None:
        return
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, name, group_name, grade, age FROM students WHERE grade = ?",
        (grade,),
    )
    print_students(cursor.fetchall())


def update_grade(conn):
    student_id = read_int("Введите ID студента: ", 1, 10**9)
    if student_id is None:
        return

    cursor = conn.cursor()
    cursor.execute("SELECT name FROM students WHERE id = ?", (student_id,))
    row = cursor.fetchone()
    if row is None:
        print(f"Студент с ID={student_id} не найден.")
        return

    grade = read_int("Введите новую оценку (2-5): ", 2, 5)
    if grade is None:
        return

    cursor.execute("UPDATE students SET grade = ? WHERE id = ?", (grade, student_id))
    conn.commit()
    print(f"Оценка студента «{row[0]}» изменена на {grade}.")


def delete_student(conn):
    student_id = read_int("Введите ID студента для удаления: ", 1, 10**9)
    if student_id is None:
        return

    cursor = conn.cursor()
    cursor.execute("SELECT name FROM students WHERE id = ?", (student_id,))
    row = cursor.fetchone()
    if row is None:
        print(f"Студент с ID={student_id} не найден.")
        return

    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    print(f"Студент «{row[0]}» удалён.")
    print("Оставшиеся студенты:")
    show_all(conn)


def count_by_group(conn):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT group_name, COUNT(*) FROM students
        GROUP BY group_name
        ORDER BY group_name
    """)
    rows = cursor.fetchall()
    if not rows:
        print("Записи не найдены.")
        return
    print("-" * 40)
    print(f"{'Группа':<15}{'Кол-во студентов':<15}")
    print("-" * 40)
    for group_name, cnt in rows:
        print(f"{group_name:<15}{cnt:<15}")
    print("-" * 40)


def read_int(prompt, min_value, max_value):
    try:
        value = int(input(prompt).strip())
    except ValueError:
        print("Ошибка: нужно ввести целое число.")
        return None
    if not (min_value <= value <= max_value):
        print(f"Ошибка: число должно быть в диапазоне от {min_value} до {max_value}.")
        return None
    return value


def print_menu():
    print()
    print("====== УЧЁТ СТУДЕНТОВ ======")
    print("1. Показать всех студентов")
    print("2. Добавить студента")
    print("3. Найти студентов по группе")
    print("4. Найти студентов по оценке")
    print("5. Изменить оценку")
    print("6. Удалить студента")
    print("7. Количество студентов в каждой группе (доп.)")
    print("0. Выход")


def main():
    conn = get_connection()
    try:
        create_table(conn)
        fill_initial_data(conn)

        while True:
            print_menu()
            choice = input("Выберите пункт меню: ").strip()

            if choice == "1":
                show_all(conn)
            elif choice == "2":
                add_student(conn)
            elif choice == "3":
                find_by_group(conn)
            elif choice == "4":
                find_by_grade(conn)
            elif choice == "5":
                update_grade(conn)
            elif choice == "6":
                delete_student(conn)
            elif choice == "7":
                count_by_group(conn)
            elif choice == "0":
                print("Выход из программы. До свидания!")
                break
            else:
                print("Неверный пункт меню. Попробуйте снова.")
    finally:
        conn.close()


if __name__ == "__main__":
    main()

def show_todo_list(filename="todo.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            tasks = file.readlines()

        if not tasks:
            print("\n--- Ваш список дел пуст. ---")
        else:
            print("\n--- Ваш список дел ---")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("\n--- Список дел пока не создан. ---")


def add_task(filename="todo.txt"):
    task = input("Введите новую задачу: ").strip()
    if not task:
        print("Задача не может быть пустой!")
        return

    with open(filename, "a", encoding="utf-8") as file:
        file.write(task + "\n")
    print(f"Задача '{task}' добавлена!")


def delete_task(filename="todo.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            tasks = file.readlines()
    except FileNotFoundError:
        print("Список дел пуст!")
        return

    if not tasks:
        print("Список дел пуст!")
        return

    show_todo_list(filename)

    try:
        task_num = int(input("\nВведите номер задачи для удаления: "))
        if task_num < 1 or task_num > len(tasks):
            print("Неверный номер задачи!")
            return
    except ValueError:
        print("Пожалуйста, введите число!")
        return

    deleted_task = tasks.pop(task_num - 1)

    with open(filename, "w", encoding="utf-8") as file:
        file.writelines(tasks)

    print(f"Задача '{deleted_task.strip()}' удалена!")


def clear_todo_list(filename="todo.txt"):
    confirm = input("Вы уверены, что хотите очистить весь список? (да/нет): ").lower()
    if confirm == "да":
        with open(filename, "w", encoding="utf-8") as file:
            pass
        print("Список дел очищен!")
    else:
        print("Очистка отменена.")


def main():
    filename = "todo.txt"

    while True:
        print("\n" + "=" * 40)
        print("1. Показать список дел")
        print("2. Добавить задачу")
        print("3. Удалить задачу")
        print("4. Очистить весь список")
        print("5. Выйти")
        print("=" * 40)

        choice = input("Выберите действие (1-5): ").strip()

        if choice == "1":
            show_todo_list(filename)
        elif choice == "2":
            add_task(filename)
        elif choice == "3":
            delete_task(filename)
        elif choice == "4":
            clear_todo_list(filename)
        elif choice == "5":
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Пожалуйста, введите число от 1 до 5.")

if __name__ == "__main__":
    main()
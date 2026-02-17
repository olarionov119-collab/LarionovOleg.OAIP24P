import json
import os

DATA_FILE = "projects.json"
PROJECT_STATUSES = ["Планирование", "В работе", "Готов"]

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_data(projects):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(projects, f, ensure_ascii=False, indent=2)

def show_projects(projects):
    if not projects:
        print("Нет проектов")
        return

    for i, p in enumerate(projects, 1):
        print(f"{i}. {p['name']} - {p['status']}")

def create_project(projects):
    name = input("Название проекта: ")
    projects.append({"name": name, "status": "Планирование", "tasks": []})
    save_data(projects)
    print("Проект создан")

def add_task(projects):
    show_projects(projects)
    if not projects:
        return

    idx = int(input("Номер проекта: ")) - 1
    if 0 <= idx < len(projects):
        task = input("Название задачи: ")
        projects[idx]["tasks"].append(task)
        save_data(projects)
        print("Задача добавлена")

def show_tasks(projects):
    show_projects(projects)
    if not projects:
        return

    idx = int(input("Номер проекта: ")) - 1
    if 0 <= idx < len(projects):
        tasks = projects[idx]["tasks"]
        if tasks:
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")
        else:
            print("Нет задач")

def change_status(projects):
    show_projects(projects)
    if not projects:
        return

    idx = int(input("Номер проекта: ")) - 1
    if 0 <= idx < len(projects):
        print("Статусы: 1.Готов 2.В работе 3.Планирование")
        s = int(input("Выберите статус: "))
        if 1 <= s <= 3:
            projects[idx]["status"] = PROJECT_STATUSES[s - 1]
            save_data(projects)
            print("Статус изменен")

def main():
    projects = load_data()

    while True:
        print("\n1.Показать проекты")
        print("2.Создать проект")
        print("3.Добавить задачу")
        print("4.Показать задачи")
        print("5.Изменить статус")
        print("6.Выход")

        choice = input("Выбор: ")

        if choice == "1":
            show_projects(projects)
        elif choice == "2":
            create_project(projects)
        elif choice == "3":
            add_task(projects)
        elif choice == "4":
            show_tasks(projects)
        elif choice == "5":
            change_status(projects)
        elif choice == "6":
            break

if __name__ == "__main__":
    main()
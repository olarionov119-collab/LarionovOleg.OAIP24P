import json

books = [
    {"id": 1, "title": "Война и мир", "author": "Лев Толстой"},
    {"id": 2, "title": "Преступление и наказание", "author": "Фёдор Достоевский"},
    {"id": 3, "title": "Мастер и Маргарита", "author": "Михаил Булгаков"},
    {"id": 4, "title": "1984", "author": "Джордж Оруэлл"},
    {"id": 5, "title": "Гарри Поттер и философский камень", "author": "Джоан Роулинг"}
]

cars = [
    {"id": 1, "brand": "Toyota", "model": "Camry", "year": 2022},
    {"id": 2, "brand": "Honda", "model": "Civic", "year": 2023},
    {"id": 3, "brand": "BMW", "model": "X5", "year": 2021},
    {"id": 4, "brand": "Mercedes-Benz", "model": "E-Class", "year": 2022},
    {"id": 5, "brand": "Audi", "model": "A4", "year": 2023}
]

airplanes = [
    {"id": 1, "manufacturer": "Boeing", "model": "737", "capacity": 215, "range_km": 6300},
    {"id": 2, "manufacturer": "Airbus", "model": "A320", "capacity": 180, "range_km": 6100},
    {"id": 3, "manufacturer": "Boeing", "model": "777", "capacity": 396, "range_km": 14300},
    {"id": 4, "manufacturer": "Airbus", "model": "A380", "capacity": 853, "range_km": 15200},
    {"id": 5, "manufacturer": "Boeing", "model": "747", "capacity": 467, "range_km": 14800}
]

with open("books.json", "w", encoding="utf-8") as f:
    json.dump(books, f, ensure_ascii=False, indent=2)

with open("cars.json", "w", encoding="utf-8") as f:
    json.dump(cars, f, ensure_ascii=False, indent=2)

with open("airplanes.json", "w", encoding="utf-8") as f:
    json.dump(airplanes, f, ensure_ascii=False, indent=2)

def open_books():
    with open("books.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        for book in data:
            print(f"ID: {book['id']}, Название: {book['title']}, Автор: {book['author']}")

def open_cars():
    with open("cars.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        for car in data:
            print(f"ID: {car['id']}, Марка: {car['brand']}, Модель: {car['model']}, Год: {car['year']}")

def open_airplanes():
    with open("airplanes.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        for plane in data:
            print(f"ID: {plane['id']}, Производитель: {plane['manufacturer']}, Модель: {plane['model']}, Вместимость: {plane['capacity']}, Дальность: {plane['range_km']} км")

print("1 - Открыть файл с книгами")
print("2 - Открыть файл с машинами")
print("3 - Открыть файл с самолетами")

choice = input("Введите цифру (1, 2 или 3): ")

if choice == "1":
    open_books()
elif choice == "2":
    open_cars()
elif choice == "3":
    open_airplanes()
else:
    print("Ошибка: нужно ввести 1, 2 или 3")
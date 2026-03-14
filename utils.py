from config import BOOKS_FILE


def load_books():
    try:
        with open(BOOKS_FILE, "r", encoding="utf-8") as file:
            books = []
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(" | ")
                    if len(parts) == 2:
                        books.append({"title": parts[0], "status": parts[1]})
            return books
    except FileNotFoundError:
        return []


def save_books(books):
    with open(BOOKS_FILE, "w", encoding="utf-8") as file:
        for book in books:
            file.write(f"{book['title']} | {book['status']}\n")


def show_books(books):
    if not books:
        print("Список книг пуст.")
        return

    print("\nСписок книг:")
    for index, book in enumerate(books, start=1):
        print(f"{index}. {book['title']} — {book['status']}")


def add_book(books):
    title = input("Введите название книги: ").strip()

    if not title:
        print("Название не может быть пустым.")
        return books

    books.append({"title": title, "status": "не прочитано"})
    save_books(books)
    print("Книга добавлена.")
    return books


def find_books(books):
    query = input("Введите название для поиска: ").strip().lower()

    if not query:
        print("Поисковый запрос пустой.")
        return

    found_books = []
    for index, book in enumerate(books, start=1):
        if query in book["title"].lower():
            found_books.append((index, book))

    if not found_books:
        print("Ничего не найдено.")
        return

    print("\nНайденные книги:")
    for index, book in found_books:
        print(f"{index}. {book['title']} — {book['status']}")


def delete_book(books):
    show_books(books)

    if not books:
        return books

    choice = input("Введите номер книги для удаления: ").strip()

    if not choice.isdigit():
        print("Нужно ввести число.")
        return books

    index = int(choice) - 1

    if index < 0 or index >= len(books):
        print("Книги с таким номером нет.")
        return books

    deleted_book = books.pop(index)
    save_books(books)
    print(f"Книга '{deleted_book['title']}' удалена.")
    return books


def mark_as_read(books):
    show_books(books)

    if not books:
        return books

    choice = input("Введите номер книги, которую прочитали: ").strip()

    if not choice.isdigit():
        print("Нужно ввести число.")
        return books

    index = int(choice) - 1

    if index < 0 or index >= len(books):
        print("Книги с таким номером нет.")
        return books

    books[index]["status"] = "прочитано"
    save_books(books)
    print(f"Книга '{books[index]['title']}' отмечена как прочитанная.")
    return books
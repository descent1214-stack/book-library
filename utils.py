from config import BOOKS_FILE


def load_books():
    try:
        with open(BOOKS_FILE, "r", encoding="utf-8") as file:
            books = []
            for line in file:
                line = line.strip()
                if line:
                    books.append(line)
            return books
    except FileNotFoundError:
        return []


def save_books(books):
    with open(BOOKS_FILE, "w", encoding="utf-8") as file:
        for book in books:
            file.write(book + "\n")


def show_books(books):
    if not books:
        print("Список книг пуст.")
        return

    print("\nСписок книг:")
    for index, book in enumerate(books, start=1):
        print(f"{index}. {book}")


def add_book(books):
    title = input("Введите название книги: ").strip()

    if not title:
        print("Название не может быть пустым.")
        return books

    books.append(title)
    save_books(books)
    print("Книга добавлена.")
    return books
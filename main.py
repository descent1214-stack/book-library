from config import APP_TITLE
from utils import load_books, show_books, add_book


def main():
    books = load_books()

    while True:
        print(f"\n{APP_TITLE}")
        print("1. Показать книги")
        print("2. Добавить книгу")
        print("3. Выход")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            show_books(books)
        elif choice == "2":
            books = add_book(books)
        elif choice == "3":
            print("Выход из программы.")
            break
        else:
            print("Неверный пункт меню. Попробуйте снова.")


main()
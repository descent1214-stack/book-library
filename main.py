from config import APP_TITLE
from utils import load_books, show_books, add_book, find_books, delete_book, mark_as_read


def main():
    books = load_books()

    while True:
        print(f"\n{APP_TITLE}")
        print("1. Показать книги")
        print("2. Добавить книгу")
        print("3. Найти книгу")
        print("4. Удалить книгу")
        print("5. Отметить как прочитанную")
        print("6. Выход")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            show_books(books)
        elif choice == "2":
            books = add_book(books)
        elif choice == "3":
            find_books(books)
        elif choice == "4":
            books = delete_book(books)
        elif choice == "5":
            books = mark_as_read(books)
        elif choice == "6":
            print("Выход из программы.")
            break
        else:
            print("Неверный пункт меню. Попробуйте снова.")


main()
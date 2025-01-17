BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]

class Book:
    """
    Класс, представляющий книгу.
    """

    def __init__(self, id_: int, name: str, pages: int) -> None:
        """
        Инициализирует книгу.

        Args:
            id_ (int): Идентификатор книги.
            name (str): Название книги.
            pages (int): Количество страниц.
        """
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        """
        Возвращает строковое представление книги.
        """
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """
        Возвращает строковое представление книги для реконструкции объекта.
        """
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"


class Library:
    """
    Класс, представляющий библиотеку.
    """

    def __init__(self, books: list[Book] = None) -> None:
        """
        Инициализирует библиотеку.

        Args:
            books (list[Book], optional): Список книг. По умолчанию пустой список.
        """
        self.books = books if books is not None else []

    def get_next_book_id(self) -> int:
        """
        Возвращает идентификатор для добавления новой книги в библиотеку.

        Returns:
            int: Следующий доступный идентификатор.
        """
        if not self.books:
            return 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """
        Возвращает индекс книги в списке по её идентификатору.

        Args:
            book_id (int): Идентификатор книги.

        Returns:
            int: Индекс книги в списке.

        Raises:
            ValueError: Если книги с запрошенным id не существует.
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")




if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1









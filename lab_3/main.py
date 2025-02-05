import doctest


class Book:
    """Базовый класс книги."""

    def __init__(self, name: str, author: str) -> None:
        """
        Инициализирует книгу.

        Args:
            name (str): Название книги.
            author (str): Автор книги.
        """
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        """
        Возвращает название книги.
        """
        return self._name

    @property
    def author(self) -> str:
        """
        Возвращает автора книги.
        """
        return self._author

    def __str__(self) -> str:
        """
        Возвращает строковое представление книги.
        """
        return f"Книга: {self.name}, Автор: {self.author}"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление книги для отладки.
        """
        return f"{self.__class__.__name__}(name='{self.name}', author='{self.author}')"


class PaperBook(Book):
    """Класс для бумажной книги."""

    def __init__(self, name: str, author: str, pages: int) -> None:
        """
        Инициализирует бумажную книгу.

        Args:
            name (str): Название книги.
            author (str): Автор книги.
            pages (int): Количество страниц в книге.
        """
        super().__init__(name, author)
        self.pages = pages  # Используем свойство для проверки

    def __str__(self) -> str:
        """
        Возвращает строковое представление бумажной книги.
        """
        return f"{super().__str__()} (стр. {self.pages})"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление бумажной книги для отладки.
        """
        return f"{self.__class__.__name__}(name='{self.name}', author='{self.author}', pages={self.pages})"

    @property
    def pages(self) -> int:
        """
        Возвращает количество страниц.
        """
        return self._pages

    @pages.setter
    def pages(self, value: int) -> None:
        """
        Устанавливает количество страниц.

        Args:
            value (int): Новое количество страниц.

        Raises:
            ValueError: Если количество страниц не является положительным целым числом.

        Examples:
             >>> book = PaperBook("Test", "Author", 100)
             >>> book.pages = 200
             >>> book.pages
             200
             >>> book.pages = -1
             Traceback (most recent call last):
                 ...
             ValueError: Количество страниц должно быть положительным целым числом.

        """
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом.")
        self._pages = value


class AudioBook(Book):
    """Класс для аудиокниги."""

    def __init__(self, name: str, author: str, duration: float) -> None:
        """
        Инициализирует аудиокнигу.

        Args:
            name (str): Название книги.
            author (str): Автор книги.
            duration (float): Продолжительность аудиокниги в минутах.
        """
        super().__init__(name, author)
        self.duration = duration  # Используем свойство для проверки

    def __str__(self) -> str:
        """
        Возвращает строковое представление аудиокниги.
        """
        return f"{super().__str__()} ({self.duration:.2f} мин.)"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление аудиокниги для отладки.
        """
        return f"{self.__class__.__name__}(name='{self.name}', author='{self.author}', duration={self.duration})"

    @property
    def duration(self) -> float:
        """
        Возвращает продолжительность аудиокниги.
        """
        return self._duration

    @duration.setter
    def duration(self, value: float) -> None:
        """
        Устанавливает продолжительность аудиокниги.

        Args:
            value (float): Новая продолжительность аудиокниги.

        Raises:
            ValueError: Если продолжительность не является положительным числом.

        Examples:
            >>> audiobook = AudioBook("Test", "Author", 60.5)
            >>> audiobook.duration = 120.0
            >>> audiobook.duration
            120.0
            >>> audiobook.duration = -1
            Traceback (most recent call last):
                ...
            ValueError: Продолжительность должна быть положительным числом.

        """
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом.")
        self._duration = value


if __name__ == "__main__":
    doctest.testmod()
    # Пример использования
    paperbook = PaperBook("Гарри Поттер", "Джоан Роулинг", 320)
    print(paperbook)
    print(repr(paperbook))
    audiobook = AudioBook("Властелин Колец", "Джон Толкин", 450.5)
    print(audiobook)
    print(repr(audiobook))
    try:
        paperbook.pages = -5
    except ValueError as e:
        print(f"Ошибка: {e}")
    try:
        audiobook.duration = -10
    except ValueError as e:
        print(f"Ошибка: {e}")

class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str = "Капитанская дочка", author: str = "Пушкин", pages: int = 300):
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        if not isinstance(new_pages, int):
            raise TypeError("Кол-во страниц должно иметь тип int")
        if new_pages <= 0:
            raise ValueError("Кол-во страниц - положительное число")
        self._pages = new_pages

    def __str__(self):
        return f"Бумажная книга: {self.name}. Автор: {self.author}. Кол-во страниц: {self.pages}"


class AudioBook(Book):
    def __init__(self, name: str = "Айвенго", author: str = "Вальтер Скотт", duration: float = 3.5):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, time: float) -> None:
        if not isinstance(time, float):
            raise TypeError("Продолжительност записи должна иметь тип float")
        if time <= 0:
            raise ValueError("Продолжительность записи - положительное число")
        self._duration = time

    def __str__(self):
        return f"Аудиокнига: {self.name}. Автор: {self.author}. Продолжительность(часы): {self.duration}"


print(PaperBook())
print(AudioBook())

# Проверяем ограничения

PaperBook.pages = 300
print(PaperBook.pages)

AudioBook.duration = 3.5
print(AudioBook.duration)

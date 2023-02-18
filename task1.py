import doctest


class Proteins:
    # Написан класс Proteins, который содержит общую для всех белков функциональность - методы для получения названия и
    # последовательности белка
    """
    Реализуется класс, представляющий собой белок.
    Класс содержит методы для получения названия и последовательности белка.
    """

    def __init__(self, name: str, sequence: str):
        """
        Конструктор класса.

        :param name: Название белка.
        :param sequence: Последовательность аминокислот белка.
        """
        self._name = name
        self._sequence = sequence

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.

        :return: Строковое представление объекта.
        """
        return f"{self._name}: {self._sequence}"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта для вывода в консоль.

        :return: Строковое представление объекта.
        """
        return f"{self.__class__.__name__}(name={self._name}, sequence={self._sequence})"

    def get_name(self) -> str:
        """
        Получает названия белка.

        :return: Название белка.
        """
        return self._name

    def get_sequence(self) -> str:
        """
        Получает последовательности белка.

        :return: Последовательность аминокислот белка.
        """
        return self._sequence


class Enzymes(Proteins):
    """
    Дочерний класс, представляющий собой фермент - один из основных типов белков.
    """

    def __init__(self, name: str, sequence: str, substrate: str, reaction: str):
        """
        Конструктор класса.

        :param name: Название фермента.
        :param sequence: Последовательность аминокислот фермента.
        :param substrate: Субстрат, на который действует фермент.
        :param reaction: Реакция, которую катализирует фермент.
        """
        super().__init__(name, sequence)
        self._substrate = substrate
        self._reaction = reaction

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.

        :return: Строковое представление объекта.
        """
        return f"{self._name} ({self._substrate}): {self._reaction}"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта для вывода в консоль.

        :return: Строковое представление объекта.
        """
        return f"{self.__class__.__name__}(name={self._name}, sequence={self._sequence}, " \
               f"substrate={self._substrate}, reaction={self._reaction})"

    def get_substrate(self) -> str:
        """
        Получает субстрат

        :return: Субстрат фермента.
        """
        return self._substrate

    def catalyze(self) -> str:
        # Метод catalyze был перегружен для реализации специфической функциональности ферментов.
        """
        Катализирует реакцию.

        :return: Результат реакции, к которой применяется фермент.

        >>> enzyme = Enzymes("Лактаза","MWVLTPLSL", "лактоза", "гидролиз")
        >>> enzyme.catalyze()
        'Лактаза катализирует гидролиз углевода лактоза'
        """
        return f"{self._name} катализирует {self._reaction} углевода {self._substrate}"

    def mutate(self, mutation_site: int, new_aminoacid: str) -> str:
        # Этот метод перегрузили, чтобы показать, как можно использовать инкапсуляцию для изменения
        # внутреннего состояния объекта. Вместо изменения атрибута self._sequence извне, был написан
        # специальный метод для мутации фермента, который может контролировать изменение внутреннего состояния объекта.
        """
        Мутация фермента путем замены одной аминокислоты на другую.

        :param mutation_site: Позиция, на которой происходит замена.
        :param new_aminoacid: Новая аминокислота.

        :return: Измененная последовательность фермента.
        """
        old_aminoacid = self._sequence[mutation_site]
        self._sequence = self._sequence[:mutation_site] + new_aminoacid + self._sequence[mutation_site + 1:]
        return f"{self._name} mutated at position {mutation_site}, " \
               f"{old_aminoacid} -> {new_aminoacid}: {self._sequence}"


if __name__ == '__main__':
    doctest.testmod()

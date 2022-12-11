import doctest


class Protein_solvent_system:
    def __init__(self, protein: str, solvent: str, volume: float):
        """
        Подготовка объекта "Система белок-растворитель"

        :param protein: "Название белка"
        :param solvent: "Тип сольвента (растворителя)
        :param volume: "Объем "бокса""

        Пример:
        >>> system = Protein_solvent_system("OCT4", "Water", 1.5)
        """
        if not isinstance(protein, (str)):
            raise TypeError("Название белка должно быть типа str")
        self.protein = protein

        if not isinstance(solvent, (str)):
            raise TypeError("Название растворителя должно иметь тип str")
        self.solvent = solvent

        if not isinstance(volume, (int, float)):
            raise TypeError("Объем бокса должен быть типа int или float")
        if volume < 1:
            raise ValueError("Объем бокса должен быть больше единицы")
        self.volume = volume

    def volume_full(self) -> bool:
        """
        Метод, который проверяет заполнен ли бокс растворителем

        :return: Заполнен ли бокс растворителем

        Пример:
        >>> system = Protein_solvent_system("OCT4", "Water", 1.5)
        >>> system.volume_full()
        """
        ...

    def fill_solvent(self, concentration: float, solvent_type: str) -> None:
        """
        Заполнение бокса растворителем определенной концентрации

        :param concentration: "Концентрация растворителя"
        :param solvent_type: "Тип растворителя"

        :return: "Систему с боксом, заполненным растворителем"

        Пример:
        >>> system = Protein_solvent_system("OCT4", "Void", 1.5)
        >>> system.fill_solvent(50, "Water")
        """
        if not isinstance(concentration, (int, float)):
            raise TypeError("Концентрация должна быть типа int или float")
        if concentration <= 0:
            raise ValueError("Концентрация не может быть меньше или равной 0")

        if not isinstance(solvent_type, (str)):
            raise TypeError("Тип растворителя должен быть типа str")
        ...

if __name__ == "__main__":
    doctest.testmod()
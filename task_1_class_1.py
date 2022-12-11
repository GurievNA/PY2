import doctest


class Plasmid:
    def __init__(self, length: int, number_of_GC_pair: int):
        """
        Подготовка объекта "Плазмида"

        :param length: "Длина плазмиды"
        :param number_of_GC_pair: "Кол-во GC-пар"

        Пример:
        >>> pT181 = Plasmid(4400, 2100)
        """
        if not isinstance(length, (int)):
            raise TypeError("Длина плазмиды должна быть типа int")
        if not 1000 < length < 600000:
            raise ValueError("Кол-во пар оснований плазмиды находится в промежутке от 1 до 600 тыс.")
        self.length = length

        if not isinstance(number_of_GC_pair, (int)):
           raise TypeError("Кол-во GC-пар в плазмиде должно быть типа int")
        if not 0 < number_of_GC_pair < 0.5 * length:
           raise ValueError("Кол-во GC-пар в плазмиде должны быть положительным числом и составлять менее 50% от длины плазмиды")
        self.number_of_GC_pair = number_of_GC_pair

    def ring_molecule(self) -> bool:
        """
        Метод, который проверяет является ли плазмида кольцевой молекулой

        :return: Является ли плазмида кольцевой

        Пример:
        >>> pT181 = Plasmid(4400, 2100)
        >>> pT181.ring_molecule()
        """
        ...

    def cut_ring_molecule(self, length_ori: int) -> None:
        """
        Разрезание кольцевой плазмиды на расстоянии от ориджина

        :param length_ori: Расстояние от ориджина до разреза

        :raise ValueError: Если расстояние до ориджина меньше одной пары нуклеотидов - вызывается ошибка

        Пример:
        >>> pT181 = Plasmid(4400, 2100)
        >>> pT181.cut_ring_molecule(1500)
        """
        if not isinstance(length_ori, (int)):
            raise TypeError("Расстояние от ori до разреза должно быть типа int")
        if length_ori <= 1:
            raise ValueError("Расстояние от ori до разреза должно быть меньше одной пары нуклеотидов")
        ...

    def add_sequence(self, length_sequence:int, AT_pair: int, GC_pair: int) -> None:
        """
        Добавление к плазмиде последовательности нуклеотидов

        :param length_sequence: Длина добавляемой последовательности
        :param AT_pair: Кол-во AT-пар в последовательности
        :param GC_pair: Кол-во GC-пар в последовательности

        :return: Длину плазмиды с добавленной последовательностью

        Пример:
        >>> pT181 = Plasmid(4400,2100)
        >>> pT181.add_sequence(700,300,400)
        """
        ...

if __name__ == "__main__":
    doctest.testmod()

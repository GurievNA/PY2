import doctest


class Wave_function:
    def __init__(self, h: float, m: float):
        """
        Подготовка объекта "Нестационарная одномерная волновая функция"

        :param h: "Постоянная Планка"
        :param m: "Масса частицы"

        Пример:
        >>> Wave = Wave_function(1.05E-34, 9.109E-31)
        """
        if not isinstance(h, (int, float)):
            raise TypeError("Постоянная планка должна быть типа int или float")
        self.h = h

        if not isinstance(m, (int, str, float)):
            raise TypeError("Масса должна быть типа int или float")
        if m <= 0:
            raise ValueError("Масса должна быть больше 0")
        self.m = m

    def non_stationarity_check(self) -> bool:
        """
        Метод, который проверяет волновую функцию на стационарность

        :return: Стационарна ли заданная волновая функция

        Пример:
        >>> wave = Wave_function(1.05E-34, 9.109E-31)
        >>> wave.non_stationarity_check()
        """
        ...

    def differentiation(self, argument: str) -> str:
        """
        Метод, который дифференцирует волновую функцию по координате x

        :return: Волновая функция в виде строки

        Пример:
        >>> wave = Wave_function(1.05E-34, 9.109E-31)
        >>> wave.differentiation("x")
        """
        ...

if __name__ == "__main__":
    doctest.testmod()
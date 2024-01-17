import doctest


class Wood:
    def __init__(self, type: str, height: float):
        """
        Создание и подготовка к работе объекта "Дерево"

        :param type: Вид дерева
        :param height: Высота дерева в метрах

        Примеры:
        >>> tree = Wood('Дуб', 10.5)  # инициализация экземпляра класса
        """
        ...

    # Рост дерева
    def growth(self, age: int) -> None:
        ...

    # Падение листьев
    def leaf_drop(self) -> None:
        ...


class Metal:
    def __init__(self, typeofmetal: str, weight: float):
        """
        Создание и подготовка к работе объекта "Металл"

        :param typeofmetal: Тип металла
        :param weight: Вес металлического объекта в килограммах

        Примеры:
        >>> metal_object = Metal('Железо', 50.2)  # инициализация экземпляра класса
        """
        ...

    # Плавление металла
    def melting(self, temperature: float) -> None:
        ...

    # Создание формы
    def forming(self, form: str) -> None:
        ...

    # Теплопроводность
    def conducting_heat(self, difference_of_temperatures: float) -> float:
        ...


class Concrete:
    def __init__(self, strengh_class: str, volume: float):
        """
        Создание и подготовка к работе объекта "Бетон"

        :param strengh_class: Класс прочности бетона
        :param volume: Объем бетона в кубических метрах

        Примеры:
        >>> concrete = Concrete('B25', 30.0)  # инициализация экземпляра класса
        """
        ...

    # Процесс отвердения бетона
    def curing(self, time_of_curing: int) -> None:
        ...

    # Разрушение бетона
    def destruction(self, pressure: float) -> bool:
        ...


if __name__ == "__main__":
    doctest.testmod()

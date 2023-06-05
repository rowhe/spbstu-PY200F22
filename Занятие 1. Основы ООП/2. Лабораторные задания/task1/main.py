# Написать 3 класса с документацией и аннотацией типов

class Table:
    """class anotations"""
    def __init__(self, color: str, weight: int):
        """Данный класс описывает стол"""
        self.color = color
        self.weight = weight

    def __repr__(self):
        return f"{self.__class__.__name__}()"


class Chair:
    """Class describing Chair"""
    def __init__(self, body: str, height: int):
        """Данный классс описывает стул"""
        self.body = None
        self.init_body(body)
        self.height = None
        self.init_height(height)

    def init_body(self, body: str):
        """Инициализируем кресло"""
        ...
    def init_height(self, height: int):
        """Инициализируем высоту кресла"""
        ...


class Lamp:
    """Class describing Lamp"""
    def __init__(self, tint: str, direction: str):
        """Данный класс описывает лампу"""
        self.tint = None
        self.init_tint(tint)
        self.direction = None
        self.init_direction(direction)

    def init_tint(self, tint: str):
        """Инициализируем оттенок света лампы"""
        ...

    def init_direction(self, direction: str):
        """Инициализируем направление света лампы"""
        ...


if __name__ == "__main__":
    import doctest
    #  работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod(Chair.init_body(1,2))
    print(Lamp.__doc__)
    table = Table("red", 2)
    print(table)

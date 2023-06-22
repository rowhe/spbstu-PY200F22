class Table:
    """class describing Table"""
    def __init__(self, color: str, weight: int):
        """Данный класс описывает стол"""
        self.color = color
        self.weight = weight

    def __repr__(self):
        return f"{self.__class__.__name__}({self.color}, {self.weight})"

    def change_color(self, color: str):
        """Изменяем атрибут colof"""
        ...

    def change_weight(self, weight):
        """Изменяем аттрибут weight"""
        ...

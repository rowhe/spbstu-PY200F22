class Lamp:
    """Class describing Lamp"""
    def __init__(self, tint: str, direction: str):
        """Данный класс описывает лампу"""
        self.tint = tint
        self.direction = direction

    def change_tint(self, tint: str):
        """Изменяем аттрибут tint"""
        ...

    def change_direction(self, direction: str):
        """Изменяем аттрибут direction"""
        ...

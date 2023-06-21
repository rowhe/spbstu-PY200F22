class Chair:
    """Class describing Chair"""
    def __init__(self, body: str, height: int):
        """Данный классс описывает стул"""
        self.body = body
        self.height = height

    def change_body(self, body: str):
        """Изменяем аттрибут body"""
        ...

    def change_height(self, height: int):
        """Изменяем аттрибут height"""
        ...
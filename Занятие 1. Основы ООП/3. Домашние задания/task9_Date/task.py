
# class Date
class Date:
    """ Класс описывающий свидание"""
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    def __repr__(self):
        return f"{self.__class__.name}({self.day}/{self.month}.{self.year}"

    def __str__(self):
        return f"{self.day}/{self.month}/{self.year}"




def ""
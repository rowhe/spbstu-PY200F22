
# class Date
class Date:
    """ Класс описывающий свидание"""
    def __init__(self, day: int, month: int, year: int):
        self.day = None
        self.set_day(day)
        self.month = None
        self.set_month(month)
        self.year = None
        self.set_year(year)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.day},{self.month},{self.year})"

    def __str__(self):
        return f"{self.day}/{self.month}/{self.year}"

    def set_day(self, day: int):
        self.vali_date(day)
        self.day = day

    def set_month(self, month: int):
        self.vali_date(month)
        self.month = month

    def set_year(self, year: int):
        self.vali_date(year)
        self.year = year

    @staticmethod
    def vali_date(i: int):
        if i is not isinstance(i, int):
            print(type(i))
            raise TypeError


if __name__ == "__main__":
    date = Date(4, 4, 1977)
    print(date)
    print(date.__repr__())


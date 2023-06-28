class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )

    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year
        self.year_ = None
        self.days_ = None

        self.is_valid_date(self.day, self.month, self.year)

    def is_leap_year(self, year: int):
        """Проверяет, является ли год високосным"""
        if year % 4 == 0:
            if year % 100 != 0:
                self.year_ = 1  # реализовать метод
            elif year % 400 == 0:
                self.year_ = 1

        self.get_max_day(self.month, self.year)

    def get_max_day(self, month: int, year: int):
        """Возвращает максимальное количество дней в месяце для указанного года"""
        if self.year_ == 1:  # используя атрибут класса DAY_OF_MONTH вернуть количество дней в запрашиваемом месяце и году
            self.days_ = sum(self.DAY_OF_MONTH[1])
        else:
            self.days_ = sum(self.DAY_OF_MONTH[0])

    def is_valid_date(self, day: int, month: int, year: int):
        """Проверяет, является ли дата корректной"""
        if 0 <= month > 12:
            ValueError(f"month value must be in 1-23 range")  # проверить валидность даты
        if 0 <= day > 31:
            ValueError(f"day value must be in 1-31 range")
        if 0 <= year > 3000:
            ValueError(f"year value must be in 1-3000 range")
        self.is_leap_year(year)

    def __str__(self):
        return f"В {self.year} году {self.days_} дней"


if __name__ == "__main__":

    for i in range(1900, 3000, 1):
        date = Date(4, 4, i)
        if date.year_ == 1:
            print(date)



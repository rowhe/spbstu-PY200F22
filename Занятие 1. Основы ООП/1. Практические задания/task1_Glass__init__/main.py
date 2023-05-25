from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        self.capacity_volume = capacity_volume  # инициализировать объект "Стакан"
        self.occupied_volume = occupied_volume


if __name__ == "__main__":
    glass = Glass()  # инициализировать два объекта типа Glass
    glass.capacity_volume = 100
    glass.occupied_volume = 50


    glass2 = Glass() # попробовать инициализировать не корректные объекты
    glass.capacity_volume = "lalala"
    glass.occupied_volume = "hahaha"

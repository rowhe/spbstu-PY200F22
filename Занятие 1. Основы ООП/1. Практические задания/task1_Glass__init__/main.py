from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float], color: str, weight: [int,float]):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("wrong type")
        if capacity_volume <= 0:
            raise ValueError("wrong value")
        self.capacity_volume = capacity_volume  # инициализировать объект "Стакан"
        self.occupied_volume = occupied_volume
        self.color = color
        self.weight = weight


if __name__ == "__main__":
    glass_1 = Glass(200, 100)  # инициализировать два объекта типа Glass
    glass_2 = Glass(500, 300)  # попробовать инициализировать не корректные объекты

print(glass_1)
print(glass_2)

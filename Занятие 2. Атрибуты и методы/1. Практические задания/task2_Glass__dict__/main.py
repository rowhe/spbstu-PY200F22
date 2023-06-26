from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        print(self.__dict__)
        self.capacity_volume = capacity_volume  # объем стакана
        self.occupied_volume = occupied_volume  # объем жидкости в стакане
        print(self.__dict__)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.capacity_volume}, {self.occupied_volume})"

    def __str__(self):
        return f"Класс {self.__class__.__name__} имеет объём {self.capacity_volume} и занятый объём {self.occupied_volume}"

if __name__ == "__main__":
    glass = Glass(200, 100)
    # print(type(glass) == glass.__init__)
    # print(glass.__dict__)
    # print(glass.__repr__())
    # print(glass.__str__())

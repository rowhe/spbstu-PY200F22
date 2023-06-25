from typing import Union


# TODO  создать класс Glass
class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        self.capacity_volume = None
        self.init_capacity_volume(capacity_volume, occupied_volume)
        self.occupied_volume = None
        self.init_occupied_volume(capacity_volume, occupied_volume)

    def init_capacity_volume(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("wrong type")
        if capacity_volume < 0:
            raise ValueError("capacity_volume cannot be less 0")
        if capacity_volume < occupied_volume:
            raise ValueError("occupied_cannot be greater than capacity_volume")

        self.capacity_volume = capacity_volume

    def init_occupied_volume(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("wrong type")
        if occupied_volume < 0:
            raise ValueError("occupied_volume cannot be less 0")
        if capacity_volume < occupied_volume:
            raise ValueError("occupied_volume cannot be greater than capacity_volume")

        self.occupied_volume = occupied_volume


if __name__ == "__main__":
    glass = Glass(200, 100)  # экземпляр класса
    print(glass.capacity_volume, glass.occupied_volume)

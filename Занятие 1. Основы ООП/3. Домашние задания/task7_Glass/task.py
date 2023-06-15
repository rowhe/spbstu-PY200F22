from typing import Union


#  создать класс Glass
class Glass:
    """ Класс описывающий стакан"""
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int,float]):
        self.capacity_volume = None
        self.set_capacity(capacity_volume)
        self.occupied_volume = None
        self.set_occupied(occupied_volume)

    def set_capacity(self, capacity):
        self.capacity_volume = capacity

    def set_occupied(self, occupied):
        self.occupied_volume = occupied



if __name__ == "__main__":
    glass = Glass(200, 100)  # экземпляр класса
    print(glass.capacity_volume, glass.occupied_volume)

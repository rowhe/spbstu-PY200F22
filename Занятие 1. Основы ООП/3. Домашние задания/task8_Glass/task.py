# Добавить методы add_water и remove_water
class Glass:
    """ Класс описывающий стакан"""
    def __init__(self, capacity_volume: int, occupied_volume: int):
        self.capacity_volume = None
        self.set_capacity(capacity_volume)
        self.occupied_volume = None
        self.set_occupied(occupied_volume)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.capacity_volume},{self.occupied_volume})"

    def __str__(self):
        return f"Класс {self.__class__.__name__}, вместимость {self.capacity_volume}, заполнено {self.occupied_volume}"

    def get_capacity(self):
        return self.capacity_volume

    def get_occupied(self):
        return self.occupied_volume

    def set_capacity(self, capacity):
        self.capacity_volume = capacity

    def set_occupied(self, occupied):
        self.occupied_volume = occupied

    def add_water(self, add):
        self.occupied_volume += add

    def remove_water(self, remove):
        self.occupied_volume -= remove

    @staticmethod
    def check_values(capacity: int, occupied: int):
        if capacity < occupied:
            raise ValueError


if __name__ == "__main__":
    glass = Glass(200, 100)
    print(glass.capacity_volume, glass.occupied_volume)
    glass.add_water(10)
    print(glass.occupied_volume)
    glass.remove_water(50)
    print(glass.occupied_volume)



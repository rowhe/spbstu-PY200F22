class Glass:
    def __init__(self, capacity_volume: int, occupied_volume: int):
        print(self.__dict__)
        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume
        print(self.__dict__)

if __name__ == "__main__":
    glass = Glass(200, 100)
    print(dir(glass))
    print(glass.__class__)
    print(glass.__dict__)

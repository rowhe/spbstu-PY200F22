# написать класс Glass согласно условию

class Glass:

    def __init__(self, material):
        self.material = None
        self.set_material(material)

    def set_material(self, material):
        self.material = material

    def get_material(self):
        return self.material

    def __repr__(self):
        return f"{self.__class__.__name__}(\"{self.material}\")"

if __name__ == "__main__":
    glass = Glass("бумага")
    print(glass.get_material)

# написать класс Glass согласно условию

class Glass:

    def __init__(self, material):
        self.material = None
        self.get_material(material)

    def get_material(self, material):
        return material

    def __repr__(self):
        return f"{self.__class__.__name__}(\"{self.material}\")"

if __name__ == "__main__":
    glass = Glass("aasdfj")
    print(glass.get_material("гумага"))


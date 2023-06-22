# Написать 3 класса с документацией и аннотацией типов
from lamp import Lamp
from chair import Chair
from table import Table


if __name__ == "__main__":
    import doctest
    table = Table("red", 2)
    #  работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod(table("red", 2))
    # doctest.testmod(table(1, 2))
    print(Lamp.__doc__)
    print(table)

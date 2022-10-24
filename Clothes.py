from Product import Product
from TypeOfClothes import TypeOfClothes


class Clothes(Product, TypeOfClothes):
    def __init__(self):
        Product.__init__(self)
        self.__size = 46
        self.__type = TypeOfClothes.SHIRTS

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size >= 44 and size <=52:
            self.__amount = size

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type):
        self.__type = type

    def display_info(self):
        Product.display_info()
        print("Тип: ", self.type, "Размер: ", self.size)

class Product:
    def __init__(self, name):
        self.__name = name
        self.__width = 0.0
        self.__height = 0.0
        self.__depth = 0.0
        self.__price = 0.0
        self.__amount = 0

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if width > 0.0:
            self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height > 0.0:
            self.__height = height

    @property
    def depth(self):
        return self.__depth

    @depth.setter
    def depth(self, depth):
        if depth > 0.0:
            self.__depth = depth

    @property
    def price(self):
        return self.__price

    @price.setter
    def width(self, price):
        if price >= 0.01:
            self.__price = price

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def depth(self, amount):
        if amount > 0.0:
            self.__amount = amount

    def display_info(self):
        print("Название товара: ", self.name, "\nГабариты: ", self.width, "x", self.height, "x", self.depth,
              "\nЦена за штуку: ", self.price, "\nКоличество товара в наличии", self.amount)

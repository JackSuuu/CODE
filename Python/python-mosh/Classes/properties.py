class Product:
    def __init__(self, price):
        self.price = price

    @property # using property to hide the duplicate function in class
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("price cannot be negative")
        self.__price = value


product = Product(-10)
print(product.price)

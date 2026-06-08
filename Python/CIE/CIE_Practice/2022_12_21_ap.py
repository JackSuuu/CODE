

class APLine:
    def __init__(self, a: int, b: int, c: int):
        self.__a = a
        self.__b = b
        self.__c = c

    def getSlope(self):
        return -(self.__a / self.__b)

    def isOnLine(self, x, y):
        if self.__a * x + self.__b * y + self.__c == 0:
            return True
        else:
            return False


line1 = APLine(5, 4, -17)
slope1 = line1.getSlope()
print(slope1)
print(line1.isOnLine(5, -2))

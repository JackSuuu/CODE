

class Abs:
    __private_count = 9

    def __init__(self):
        self.public_count = 10

    def getCount(self):
        return self.__private_count


a = Abs()
print(a.getCount())
# print(a.public_count)

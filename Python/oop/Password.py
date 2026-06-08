from random import randint


# python 里面使用静态变量
class PasswordGenerator:
    _count = 0

    def __init__(self, length: int, prefix='A'):
        self.length = length
        self.prefix = prefix

    @staticmethod
    def pwCount():
        return PasswordGenerator._count

    def pwGen(self):
        password = ''
        password += (self.prefix + '.')
        PasswordGenerator._count += 1
        for i in range(self.length):
            password += str(randint(0, 9))
        return password


pw1 = PasswordGenerator(4, "chs")
print(pw1.pwCount())
print(pw1.pwGen())
print(pw1.pwGen())
print(pw1.pwCount())
pw2 = PasswordGenerator(6)
print(pw2.pwGen())
print(pw2.pwCount())
print(pw2.pwCount())

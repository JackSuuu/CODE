import random


class RandomStringChooser:
    def __init__(self, str_arr=None):
        if str_arr is None:
            str_arr = []
        self.str_arr = str_arr

    def getNext(self):
        length = len(self.str_arr)
        if length == 0:
            return "NONE"
        else:
            random_i = random.randint(0, length - 1)
            return self.str_arr.pop(random_i)


class StringChooser(RandomStringChooser):
    super.__init__()

    def getNext(self):
        pass


RandomStringChooser_arr = ["wheels", "on", "the", "bus"]
sChooser = RandomStringChooser(RandomStringChooser_arr)
for i in range(6):
    print(sChooser.getNext())

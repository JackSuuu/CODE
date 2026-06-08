class Point:
    def __init__(self, x, y):  # constructors
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Point({self.x}, {self.y})")


point = Point.zero()   #factory method 工厂函数
point.draw()


        

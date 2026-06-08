# Class: blueprint for creating new objects
# Object: instance of a class

# Class: human
# Objects: John, Mary, Jack,

# print(type(point))
# print(isinstance(point, Point))

class Point:
    default_color = "red"

    def __init__(self, x, y):  # constructors
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point({self.x}, {self.y})")

Point.default_color = "yellow"

point = Point(1, 2)
print(point.default_color)
print(Point.default_color)
point.draw()

another = Point(3, 4)
another.draw()

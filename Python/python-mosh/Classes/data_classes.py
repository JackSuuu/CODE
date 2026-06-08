from collections import namedtuple

# when writing classes that only render data
Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)
p2 = Point(1, 2)
print(p1 == p2)

class SingleTable:
    # private seats: integer
    # private heights: integer
    # private views: integer
    def __init__(self, seats, heights, views):
        self.__seats = seats
        self.__heights = heights
        self.__views = views

    # Returns the number of seats at this table. The value is always greater than or equal to 4.
    def getNumSeats(self):
        return self.__seats

    # Returns the height of this table in centimeters.
    def getHeight(self):
        return self.__heights

    # Returns the quality of the view from this table.
    def getViewQuality(self):
        return self.__views

    # Sets the quality of the view from this table to value .
    def setViewQuality(self, value):
        self.__views = value


class CombinedTable:
    def __init__(self, t1: SingleTable, t2: SingleTable):
        self.new_seat = (t1.getNumSeats() + t2.getNumSeats()) - 2
        self.t1 = t1
        self.t2 = t2

    def canSeat(self, number):
        if number <= self.new_seat:
            return True
        else:
            return False

    def getDesirability(self):
        if self.t1.getHeight() == self.t2.getHeight():
            return (self.t1.getViewQuality() + self.t2.getViewQuality()) / 2
        else:
            return ((self.t1.getViewQuality() + self.t2.getViewQuality()) / 2) - 10


table1 = SingleTable(4, 74, 60)
table2 = SingleTable(8, 74, 70)
table3 = SingleTable(12, 76, 75)
c1 = CombinedTable(table1, table2)
c2 = CombinedTable(table2, table3)

# print(c1.canSeat(9))
# print(c1.canSeat(11))
# print(c1.getDesirability)

print(c2.canSeat(18))
print(c2.getDesirability())
table2.setViewQuality(80)
print(c2.getDesirability())

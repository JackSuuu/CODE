from enum import Enum

class Weekday(Enum):
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5
    Saturday = 6
    Sunday = 7

c = Weekday(int(input("Please inpput day in a week")))
print(c)

if c.value > Weekday.Friday.value:
    print("Today is weekend")
else:
    print("Normal week")
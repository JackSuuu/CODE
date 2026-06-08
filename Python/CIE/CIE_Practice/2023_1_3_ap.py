
class StepTracker:
    # private active_day: integer
    # private steps: integer
    # private days: integer
    def __init__(self, active_day: int):
        self.__active_day = active_day
        self.__steps = 0
        self.__days = 0
        self.__active = 0

    def addDailySteps(self, day_steps: int):
        self.__steps += day_steps
        self.__days += 1
        if day_steps >= self.__active_day:
            self.__active += 1

    def activeDays(self):
        return self.__active

    def averageSteps(self):
        if self.__days != 0:
            return self.__steps / self.__days
        else:
            return 0


tr = StepTracker(10000)
print(tr.activeDays())
print(tr.averageSteps())

tr.addDailySteps(9000)
tr.addDailySteps(5000)
print(tr.activeDays())
print(tr.averageSteps())

tr.addDailySteps(13000)
print(tr.activeDays())
print(tr.averageSteps())

tr.addDailySteps(23000)
tr.addDailySteps(1111)
print(tr.activeDays())
print(tr.averageSteps())

class Employee:
    def greet(self):
        print("Employee Greet")


class Person:
    def greet(self):
        print("Person Greet")


class Manager(Employee, Person):
    pass


M = Manager()
M.greet()
# result print out the Employee greet, because the Employee inherit first
# Multiple inheritance when classes are small and features are different

# An example of good inheritance


class Flyer:
    def fly(self):
        pass


class Swimmer:
    def swim(self):
        pass


class FlyingFish(Flyer, Swimmer):
    pass


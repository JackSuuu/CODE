class Animal(object):
    def __init__(self):
        print("Animal Constructor")
        self.age = 1

    def eat(self):
        print("eat")

# refer Animal : parent
# Mammal: Child
class Mammal(Animal):
    def __init__(self): # constructor
        print("Mammal Constructor")
        self.weight = 2 # method overridding
        super().__init__() # the position of the super function decided the sequence of the inheritance

    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")

o = object()
print(issubclass(Mammal, Animal))
m = Mammal()
print(m.age)
print(m.weight)

cat = Animal()
cat.eat()


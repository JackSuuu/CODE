class Animal:
    def eat(self):
        print("eat")


class Brid(Animal):
    def fly(self):
        print("fly")


class Chicken(Brid): # inheritance abuse, Chicken cannot fly
    pass

# Employee - Person - LivingCreature - Thing
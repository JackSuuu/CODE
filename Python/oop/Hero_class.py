
import random


class Hero:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def seeHealth(self):
        print(f"{self.name}'s current health is {self.health}")

    def attack(self, hero, damage):
        if damage <= hero.health:
            hero.health -= damage
            print(
                f"{hero.name} is under attack by {self.name}, {hero.name}'s health is now {hero.health}")
        else:
            self.health = 0
            print(f"{self.name} is dead already")

    def cure(self, value):
        if value <= self.health < 100:
            self.health += value
            print(f"current health is {self.health}")


class StrengthHero(Hero):
    # Use random to generate the percentage of multiple_attack
    multiple_attack = random.randint(0, 100) / 100
    is_multiple = random.randint(0, 1)

    def __init__(self, name, multiple, health=100):
        super().__init__(name, health)
        self.multiple_attack = multiple

    def attack(self, hero, damage):
        if damage <= hero.health:
            if self.is_multiple == 1:
                hero.health -= damage * self.multiple_attack
                print(f"{hero.name}, is under attack ~, multiple attack applied.")
                print(f"{hero.name} current health is {hero.health}")
            else:
                hero.health -= damage
                print(f"{hero.name} current health is {hero.health}")
        else:
            hero.health = 0
            print(f"{self.name} is dead already")


Hero_1 = Hero("Sheldon")
Hero_2 = Hero("Jake")
Hero_3 = StrengthHero("David", 2, 300)

print(Hero_3.name)
Hero_3.attack(Hero_2, 10)

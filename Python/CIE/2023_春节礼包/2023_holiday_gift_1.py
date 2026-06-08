
# Meal and DeluxeMeal class
class Meal:
    # Private food_name: string
    # Private food_cost: integer
    def __init__(self, food_name: str, food_cost: float):
        self.__food_name = food_name
        self.__food_cost = food_cost

    def getFoodName(self):
        return self.__food_name

    def getFoodCost(self):
        return self.__food_cost

    def toString(self):
        return f'{self.__food_name} meal, ${self.__food_cost}'


burger = Meal("hamburger", 7.99)
print(burger.toString())


class DeluxeMeal(Meal):
    def __init__(self, food_name: str, side_dish: str, drink: str, food_cost: float):
        super().__init__(food_name, food_cost)
        self.side_dish = side_dish
        self.drink = drink

    def toString(self):
        return f'deluxe {self.getFoodName()} meal, ${self.getFoodCost() + 3}'


burritoCombo = DeluxeMeal("burrito", "chips", "lemonade", 7.49)
print(burritoCombo.toString())

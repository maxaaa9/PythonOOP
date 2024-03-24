from project.animals.animal import Mammal
from project.food import Meat, Vegetable, Fruit, Seed


class Mouse(Mammal):

    def make_sound(self) -> str:
        return "Squeak"

    @property
    def food_that_eat(self) -> list:
        return [Vegetable, Fruit]

    @property
    def weight_increase(self):
        return 0.10


class Dog(Mammal):

    def make_sound(self) -> str:
        return "Woof!"

    @property
    def food_that_eat(self) -> list:
        return [Meat]

    @property
    def weight_increase(self):
        return 0.40


class Cat(Mammal):

    def make_sound(self) -> str:
        return "Meow"

    @property
    def food_that_eat(self) -> list:
        return [Vegetable, Meat]

    @property
    def weight_increase(self):
        return 0.30


class Tiger(Mammal):

    def make_sound(self) -> str:
        return "ROAR!!!"

    @property
    def food_that_eat(self) -> list:
        return [Meat]

    @property
    def weight_increase(self):
        return 1.00

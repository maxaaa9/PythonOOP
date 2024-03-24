from project.animals.animal import Bird
from project.food import Meat, Vegetable, Fruit, Seed


class Owl(Bird):

    def make_sound(self) -> str:
        return "Hoot Hoot"

    @property
    def food_that_eat(self) -> list:
        return [Meat]

    @property
    def weight_increase(self):
        return 0.25


class Hen(Bird):

    def make_sound(self) -> str:
        return "Cluck"

    @property
    def food_that_eat(self) -> list:
        return [Meat, Vegetable, Fruit, Seed]

    @property
    def weight_increase(self):
        return 0.35

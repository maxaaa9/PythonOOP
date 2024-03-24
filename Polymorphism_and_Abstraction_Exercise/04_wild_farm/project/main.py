from project.food import Food, Meat, Vegetable
from project.animals.animal import Animal
from project.animals.birds import Bird, Owl
from project.animals.mammals import Mammal

owl = Owl("Pip", 10, 10)
print(owl)
meat = Meat(4)
print(owl.make_sound())
owl.feed(meat)
veg = Vegetable(1)
print(owl.feed(veg))
print(owl)
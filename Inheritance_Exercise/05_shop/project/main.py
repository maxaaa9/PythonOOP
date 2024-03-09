from project.product_repository import ProductRepository
from project.food import Food
from project.drink import Drink


food = Food("apple")
drink = Drink("water")
repo = ProductRepository()
repo.add(food)
repo.add(drink)
repo.remove("apple")
print(repo.products)
print(repo.find("water"))
repo.find("apple").decrease(5)
print(repo)




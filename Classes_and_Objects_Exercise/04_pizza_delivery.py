class PizzaDelivery:

    def __init__(self, name: str, price: float, ingredients: dict):
        self.ordered = False
        self.name = name
        self.price = price
        self.ingredients = ingredients

    def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float):
        if self.ordered:
            return PizzaDelivery.pizza_ordered(self)

        if ingredient in self.ingredients.keys():
            self.ingredients[ingredient] += quantity

        else:
            self.ingredients[ingredient] = quantity

        self.price += price_per_quantity * quantity

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float) -> str:
        if self.ordered:
            return PizzaDelivery.pizza_ordered(self)

        if ingredient not in self.ingredients.keys():
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"

        elif quantity > self.ingredients[ingredient]:
            return f"Please check again the desired quantity of {ingredient}!"

        else:
            self.ingredients[ingredient] -= quantity
            self.price -= quantity * price_per_quantity

    def make_order(self):
        self.ordered = True
        return (f"You've ordered pizza {self.name} prepared with "
                f"{', '.join(f'{k}: {v}' for k, v in self.ingredients.items())} "
                f"and the price will be {self.price}lv.")

    def pizza_ordered(self):
        return f"Pizza {self.name} already prepared, and we can't make any changes!"

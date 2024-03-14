from typing import Dict


class Shop:

    def __init__(self,name: str, _type: str, capacity: int):
        self.name = name
        self.type = _type
        self.capacity = capacity
        self.items: Dict[str: int] = {}

    @classmethod
    def small_shop(cls, name: str, _type: str):
        return cls(name, _type, 10)

    def add_item(self, item_name: str):
        if sum(self.items.values()) < self.capacity:
            if item_name not in self.items.keys():
                self.items[item_name] = 0

            self.items[item_name] += 1
            return f"{item_name} added to the shop"
        else:
            return "Not enough capacity in the shop"

    def remove_item(self, item_name: str, amount: int):
        product_quantity = self.items.get(item_name)

        if not product_quantity or amount > product_quantity:
            return f"Cannot remove {amount} {item_name}"
        # try:
        #     self.items[item_name] -= amount
        #
        # except Exception:
        #     return f"Cannot remove {amount} {item_name}"

        self.items[item_name] -= amount

        if self.items[item_name] <= 0:
            del self.items[item_name]

        return f"{amount} {item_name} removed from the shop"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"
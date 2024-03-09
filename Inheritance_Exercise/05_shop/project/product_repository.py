from typing import List

from project.product import Product


class ProductRepository:

    def __init__(self):
        self.products: List[Product] = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, product_name: str) -> str or None:
        try:
            find_product = next(filter(lambda p: p.name == product_name, self.products))
            return find_product
        except StopIteration:
            return None

    def remove(self, product_name: str) -> None:
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)

    def __repr__(self):
        return '\n'.join(f"{p.name}: {p.quantity}" for p in self.products)



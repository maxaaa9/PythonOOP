from typing import List

from project.customer import Customer
from project.dvd import DVD


class MovieWorld:

    def __init__(self, name: str):
        self.name = name
        self.customers: List[Customer] = []  # Customer Objects
        self.dvds: List[DVD] = []   # DVD Objects

    @staticmethod
    def dvd_capacity() -> int:
        return 15

    @staticmethod
    def customer_capacity() -> int:
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        try:
            customer = next(filter(lambda c: c.id == customer_id, self.customers))
        except StopIteration:
            return

        try:
            dvd = next(filter(lambda d: d.id == dvd_id, self.dvds))
        except StopIteration:
            return

        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"

        if dvd.is_rented:
            return "DVD is already rented"

        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int):
        customer_name = next(filter(lambda c: c.id == customer_id, self.customers))
        dvd_name = next(filter(lambda d: d.id == dvd_id, self.dvds))

        if dvd_name in customer_name.rented_dvds:
            customer_name.rented_dvds.remove(dvd_name)
            dvd_name.is_rented = False
            return f"{customer_name.name} has successfully returned {dvd_name.name}"

        return f"{customer_name.name} does not have that DVD"

    def __repr__(self):
        str_info = ""
        for customer in self.customers:
            str_info += f"{customer.__repr__()}\n"
        for dvd in self.dvds:
            str_info += f"{dvd.__repr__()}\n"

        return str_info

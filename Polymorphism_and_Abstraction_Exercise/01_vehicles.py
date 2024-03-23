from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, km_to_traveling: int) -> None:
        ...

    @abstractmethod
    def refuel(self, quantity: int) -> None:
        ...


class Car(Vehicle):
    AIR_CONDITIONER_CONSUMPTION: float = 0.9

    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, km_to_traveling: float):
        needed_fuel = (self.fuel_consumption + self.AIR_CONDITIONER_CONSUMPTION) * km_to_traveling
        if needed_fuel <= self.fuel_quantity:
            self.fuel_quantity -= needed_fuel

    def refuel(self, quantity: float):
        self.fuel_quantity += quantity


class Truck(Vehicle):
    AIR_CONDITIONER_CONSUMPTION = 1.6
    TANK_HOLE = 0.95    # This will be used to decrease 5% of refueled quantity

    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, km_to_traveling: float):
        needed_fuel = (self.fuel_consumption + self.AIR_CONDITIONER_CONSUMPTION) * km_to_traveling
        if needed_fuel <= self.fuel_quantity:
            self.fuel_quantity -= needed_fuel

    def refuel(self, quantity):
        self.fuel_quantity += quantity * self.TANK_HOLE


truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)

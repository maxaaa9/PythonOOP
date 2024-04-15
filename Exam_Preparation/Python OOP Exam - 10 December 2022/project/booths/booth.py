from typing import List

from abc import ABC, abstractmethod

from project.delicacies.delicacy import Delicacy


class Booth(ABC):

    def __init__(self, booth_number: int,  capacity: int):
        self.booth_number = booth_number
        self.capacity = capacity
        self.delicacy_orders: List[Delicacy] = []
        self.__price_for_reservation: float = 0
        self.is_reserved: bool = False

    @property
    def price_for_reservation(self):
        return self.__price_for_reservation

    @price_for_reservation.setter
    def price_for_reservation(self, value):
        self.__price_for_reservation = float(value)

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("Capacity cannot be a negative number!")

        self.__capacity = value

    @abstractmethod
    def reserve(self, number_of_people: int):
        pass

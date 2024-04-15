from project.booths.booth import Booth


class PrivateBooth(Booth):
    RESERVATION_PRICE = 3.50

    def __init__(self, booth_number: int, capacity: int):
        super(PrivateBooth, self).__init__(booth_number, capacity)

    def reserve(self, number_of_people: int):
        self.price_for_reservation = number_of_people * self.RESERVATION_PRICE
        self.is_reserved = True

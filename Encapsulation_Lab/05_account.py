class Account:

    def __init__(self, _id: int, balance: int, pin: int):
        self.__id = _id
        self.balance = balance
        self.__pin = pin

    def get_id(self, pin) -> int or str:
        return self.__id if pin == self.__pin else "Wrong pin"

    def change_pin(self, old_pin: int, new_pin: int) -> str:
        if old_pin == self.__pin:
            self.__pin = new_pin
            return "Pin changed"
        return "Wrong pin"
from project.delicacies.delicacy import Delicacy


class Gingerbread(Delicacy):
    PORTION_WEIGHT = 200

    def __init__(self, name: str, price: float):
        super(Gingerbread, self).__init__(name, self.PORTION_WEIGHT, price)

    def details(self):
        return f"Gingerbread {self.name}: {self.PORTION_WEIGHT}g - {self.price:.2f}lv."

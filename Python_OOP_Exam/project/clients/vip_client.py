from project.clients.base_client import BaseClient


class VIPClient(BaseClient):
    TYPE = "VIP"
    PRICE_PER_POINT = 5

    def __init__(self, name: str):
        super().__init__(name, self.TYPE)

    def earning_points(self, order_amount: float):
        earned_points = order_amount // self.PRICE_PER_POINT
        self.total_earned_points += earned_points
        self.points += earned_points
        return int(earned_points)


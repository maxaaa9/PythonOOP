from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    INITIAL_OXYGEN = 540

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_OXYGEN)

    def miss(self, time_to_catch: int):
        result = self.oxygen_level - round(time_to_catch * 0.3)
        if result < 0:
            self.oxygen_level = 0
        else:
            self.oxygen_level = result

    def renew_oxy(self):
        self.oxygen_level = self.INITIAL_OXYGEN



from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class ArcticClimber(BaseClimber):
    DECREASE_STRENGTH = 20

    def __init__(self, name: str):
        super().__init__(name, 200)

    def can_climb(self):
        if self.strength >= 100:
            return True
        return False

    def climb(self, peak: BasePeak):
        if peak.difficulty_level == "Extreme":
            self.strength -= self.DECREASE_STRENGTH * 2.0
        else:
            self.strength -= self.DECREASE_STRENGTH * 1.5

        self.conquered_peaks.append(peak.name)

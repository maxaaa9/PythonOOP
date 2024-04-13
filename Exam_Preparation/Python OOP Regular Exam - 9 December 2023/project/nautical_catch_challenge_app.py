from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish
from project.divers.base_diver import BaseDiver
from project.fish.base_fish import BaseFish


class NauticalCatchChallengeApp:
    VALID_DIVER_TYPES = {"FreeDiver": FreeDiver,
                         "ScubaDiver": ScubaDiver}

    VALID_FISH_TYPES = {"PredatoryFish": PredatoryFish,
                        "DeepSeaFish": DeepSeaFish}

    def __init__(self):
        self.divers = []
        self.fish_list = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in self.VALID_DIVER_TYPES:
            return f"{diver_type} is not allowed in our competition."

        try:
            next(filter(lambda d: d.name == diver_name, self.divers))
            return f"{diver_name} is already a participant."
        except StopIteration:
            self.divers.append(self.VALID_DIVER_TYPES[diver_type](diver_name))
            return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self.VALID_FISH_TYPES:
            return f"{fish_type} is forbidden for chasing in our competition."

        try:
            next(filter(lambda f: f.name == fish_name, self.fish_list))
            return f"{fish_name} is already permitted."
        except StopIteration:
            self.fish_list.append(self.VALID_FISH_TYPES[fish_type](fish_name, points))
            return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        try:
            diver = next(filter(lambda d: d.name == diver_name, self.divers))
        except StopIteration:
            return f"{diver_name} is not registered for the competition."

        try:
            fish = next(filter(lambda f: f.name == fish_name, self.fish_list))
        except StopIteration:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            message = f"{diver_name} missed a good {fish_name}."

        elif diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                message = f"{diver_name} hits a {fish.points}pt. {fish_name}."
            else:
                diver.miss(fish.time_to_catch)
                message = f"{diver_name} missed a good {fish_name}."

        else:
            diver.hit(fish)
            message = f"{diver_name} hits a {fish.points}pt. {fish_name}."

        if diver.oxygen_level == 0:
            diver.has_health_issue = True

        return message

    def health_recovery(self):
        recovered_divers = 0
        for diver in self.divers:
            if diver.has_health_issue:
                diver.has_health_issue = False
                diver.renew_oxy()
                recovered_divers += 1
        return f"Divers recovered: {recovered_divers}"

    def diver_catch_report(self, diver_name: str):
        diver = next(filter(lambda d: d.name == diver_name, self.divers))
        my_output = f"**{diver_name} Catch Report**"
        for fish in diver.catch:
            my_output += f"\n{fish.fish_details()}"

        return my_output

    def competition_statistics(self):
        sorted_divers = sorted(self.divers, key=lambda cp: (-cp.competition_points, -len(cp.catch), cp.name))
        output = "**Nautical Catch Challenge Statistics**"
        for diver in sorted_divers:
            if not diver.has_health_issue:
                output += f"\n{str(diver)}"

        return output

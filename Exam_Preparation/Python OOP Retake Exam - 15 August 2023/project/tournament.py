from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    VALID_EQUIPMENT_TYPES = {"KneePad": KneePad,
                             "ElbowPad": ElbowPad}

    VALID_TEAM_TYPES = {"OutdoorTeam": OutdoorTeam,
                        "IndoorTeam": IndoorTeam}

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment = []
        self.teams = []
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")

        self.__name = value

    def add_equipment(self, equipment_type: str):
        if equipment_type not in self.VALID_EQUIPMENT_TYPES.keys():
            raise Exception("Invalid equipment type!")

        self.equipment.append(self.VALID_EQUIPMENT_TYPES[equipment_type]())
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.VALID_TEAM_TYPES.keys():
            raise Exception("Invalid team type!")

        if not self.capacity:
            return "Not enough tournament capacity."

        self.capacity -= 1
        self.teams.append(self.VALID_TEAM_TYPES[team_type](team_name, country, advantage))

        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        equipment_obj = next(filter(lambda e: e.__class__.__name__ == equipment_type, reversed(self.equipment)))
        team_obj = next(filter(lambda t: t.name == team_name, self.teams))

        if team_obj.budget < equipment_obj.PRICE:
            raise Exception("Budget is not enough!")

        team_obj.budget -= equipment_obj.PRICE
        self.equipment.remove(equipment_obj)
        team_obj.equipment.append(equipment_obj)
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        try:
            team = next(filter(lambda t: t.name == team_name, self.teams))
        except StopIteration:
            raise Exception("No such team!")

        if team.wins:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")

        self.capacity += 1
        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        eq_list = [x.increase_price() for x in self.equipment if x.__class__.__name__ == equipment_type]
        return f"Successfully changed {len(eq_list)}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team1 = next(filter(lambda t1: t1.name == team_name1, self.teams))
        team2 = next(filter(lambda t2: t2.name == team_name2, self.teams))

        if team1.__class__.__name__ != team2.__class__.__name__:
            raise Exception("Game cannot start! Team types mismatch!")

        team1_total_protection = sum([x.protection for x in team1.equipment])
        team2_total_protection = sum([x.protection for x in team2.equipment])

        team1_total_score = team1.advantage + team1_total_protection
        team2_total_score = team2.advantage + team2_total_protection

        if team1_total_score == team2_total_score:
            return "No winner in this game."

        winner = team1 if team1_total_score > team2_total_score else team2
        winner.win()

        return f"The winner is {winner.name}."

    def get_statistics(self):
        sorted_teams = sorted(self.teams, key=lambda w: -w.wins)
        my_output = f"Tournament: {self.name}\n" \
                    f"Number of Teams: {len(self.teams)}\n" \
                    f"Teams:"

        for team in sorted_teams:
            my_output += f"\n{team.get_statistics()}"

        return my_output

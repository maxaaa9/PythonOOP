from project.formula_teams.mercedes_team import MercedesTeam
from project.formula_teams.red_bull_team import RedBullTeam


class F1SeasonApp:

    def __init__(self):
        self.red_bull_team = None
        self.mercedes_team = None

    @staticmethod
    def valid_team(team_name):
        return f"{team_name} has joined the new F1 season."

    def register_team_for_season(self, team_name: str, budget: int):
        if team_name == "Mercedes":
            self.mercedes_team = MercedesTeam(budget)
            return self.valid_team(team_name)

        elif team_name == "Red Bull":
            self.red_bull_team = RedBullTeam(budget)
            return self.valid_team(team_name)

        raise ValueError("Invalid team name!")

    def new_race_results(self, race_name: str, red_bull_pos: int, mercedes_pos: int):
        if self.red_bull_team is None or self.mercedes_team is None:
            raise Exception("Not all teams have registered for the season.")

        better_team = "Mercedes" if mercedes_pos < red_bull_pos else "Red Bull"

        red_bull_revenue: str = self.red_bull_team.calculate_revenue_after_race(red_bull_pos)
        mercedes_revenue: str = self.mercedes_team.calculate_revenue_after_race(mercedes_pos)

        return (
            f"Red Bull: {red_bull_revenue}. "
            f"Mercedes: {mercedes_revenue}. "
            f"{better_team} is ahead at the {race_name} race.")
        #
        # return (f"Red Bull: {RedBullTeam.calculate_revenue_after_race(red_bull_pos)}. "
        #         f"Mercedes: {MercedesTeam.calculate_revenue_after_race(mercedes_pos)}. "
        #         f"{better_team} is ahead at the {race_name} race.")


from project.player import Player


class Guild:

    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player: Player) -> str:
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."

        if player.guild == "Unaffiliated":
            player.guild = self.name
            self.players.append(player)
            return f"Welcome player {player.name} to the guild {self.name}"

        return f"Player {player.name} is in another guild."

    def kick_player(self, player_name: str) -> str:
        # try:
        #     player = next(filter(lambda p: p.name == player_name, self.players))
        # except StopIteration:
        #     return f"Player {player_name} is not in the guild."
        for player in self.players:
            if player.name == player_name:
                player.guild = "Unaffiliated"
                self.players.remove(player)
                return f"Player {player_name} has been removed from the guild."

        return f"Player {player_name} is not in the guild."
        # player.guild = "Unaffiliated"
        # self.players.remove(player)
        #
        # return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        guild_players = '\n'.join(player.player_info() for player in self.players)
        return f"Guild: {self.name}\n" \
               f"{guild_players}"




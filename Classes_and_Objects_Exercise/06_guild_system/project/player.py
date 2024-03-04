class Player:

    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name: str, mana_cost: int):
        if self.skills.get(skill_name):
            return "Skill already added"

        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        skills_mp_dict_as_str = '\n'.join(f'==={s} - {m}' for s, m in self.skills.items())
        player_info = f"Name: {self.name}\n" \
                      f"Guild: {self.guild}\n" \
                      f"HP: {self.hp}\n" \
                      f"MP: {self.mp}\n" \
                      f"{skills_mp_dict_as_str}"
        return player_info




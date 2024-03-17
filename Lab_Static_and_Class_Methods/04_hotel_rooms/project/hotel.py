from project.room import Room


class Hotel:

    def __init__(self, name: str):
        self.name = name
        self.guests = 0
        self.rooms = []

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int):
        try:
            room = next(filter(lambda r: r.number == room_number, self.rooms))
        except StopIteration:
            return

        result = room.take_room(people)

        if not result:
            self.guests += people

    def free_room(self, room_number: int):
        try:
            free_room = next(filter(lambda f: f.is_taken == room_number, self.rooms))
        except StopIteration:
            return

        people = free_room.guests
        result = free_room.free_room()

        if not result:
            self.guests -= people

    def status(self):
        return f"Hotel {self.name} has {self.guests} total guests\n"\
                f"Free rooms: {', '.join(str(x.number) for x in self.rooms if not x.is_taken)}\n"\
                f"Taken rooms: {', '.join(str(x.number) for x in self.rooms if x.is_taken)}"



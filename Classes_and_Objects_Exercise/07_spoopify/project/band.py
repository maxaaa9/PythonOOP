from project.album import Album


class Band:

    def __init__(self, name: str):
        self.albums = []
        self.name = name

    def add_album(self, album: Album) -> str:
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."

        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str) -> str:
        for album in self.albums:
            if album.published and album.name == album_name:
                return "Album has been published. It cannot be removed."
            if album_name == album.name:
                self.albums.remove(album)
                return f"Album {album_name} has been removed."

        return f"Album {album_name} is not found."

    def details(self):
        band_string = '\n'.join(a.details() for a in self.albums)
        return (f"Band {self.name}\n"
                f"{band_string}")

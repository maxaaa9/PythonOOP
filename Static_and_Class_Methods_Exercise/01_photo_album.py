from math import ceil
from typing import List


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4
    TOTAL_SYMBOLS = 11
    SYMBOL = "-"

    def __init__(self, pages: int):
        self.pages = pages
        self.photos: List[List[str]] = [[] for _ in range(self.pages)]      # pages

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / cls.PHOTOS_PER_PAGE))

    def add_photo(self, label: str):
        for page in range(self.pages):
            if len(self.photos[page]) < self.PHOTOS_PER_PAGE:
                slot = len(self.photos[page]) + 1
                self.photos[page].append(label)

                return f"{label} photo added successfully on page " \
                       f"{page + 1} slot {slot}"

        return "No more free slots"

    def display(self):
        my_output_str = ""
        dashes = f"{self.TOTAL_SYMBOLS * self.SYMBOL}"
        for page in range(self.pages):
            if not page:
                my_output_str += dashes
            my_output_str += f"\n{('[] ' * len(self.photos[page])).rstrip()}" \
                             f"\n{dashes}"

        return my_output_str


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())

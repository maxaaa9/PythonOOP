from project.mammal import Mammal
from unittest import TestCase, main


class TestMammal(TestCase):

    def setUp(self) -> None:
        self.test_mammal = Mammal("Gosho", "pig", "Kweek")

    def test_init(self):
        self.assertEqual("Gosho", self.test_mammal.name)
        self.assertEqual("pig", self.test_mammal.type)
        self.assertEqual("Kweek", self.test_mammal.sound)
        self.assertEqual("animals", self.test_mammal.get_kingdom())

    def test_make_sound(self):
        self.assertEqual("Gosho makes Kweek", self.test_mammal.make_sound())

    def test_info_return(self):
        self.assertEqual("Gosho is of type pig", self.test_mammal.info())


if __name__ == "__main__":
    main()
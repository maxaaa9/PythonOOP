from unittest import TestCase, main

from project.toy_store import ToyStore


class TestToyStore(TestCase):

    def setUp(self) -> None:
        self.test_store = ToyStore()

    def test_init(self):
        self.assertIsNone(self.test_store.toy_shelf["A"])
        self.assertIsNone(self.test_store.toy_shelf["B"])
        self.assertIsNone(self.test_store.toy_shelf["C"])
        self.assertIsNone(self.test_store.toy_shelf["D"])
        self.assertIsNone(self.test_store.toy_shelf["E"])
        self.assertIsNone(self.test_store.toy_shelf["F"])
        self.assertIsNone(self.test_store.toy_shelf["G"])

    def test_add_toy_with_invalid_shelf(self):
        with self.assertRaises(Exception) as ex:
            self.test_store.add_toy("Z", "Dolly")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_with_same_toy(self):
        self.test_store.toy_shelf["A"] = "Car"
        with self.assertRaises(Exception) as ex:
            self.test_store.add_toy("A", "Car")

        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_at_taken_shelf(self):
        self.test_store.toy_shelf["C"] = "Car"
        with self.assertRaises(Exception) as ex:
            self.test_store.add_toy("C", "Book")

        self.assertEqual("Shelf is already taken!", str(ex.exception))
        self.assertIsNotNone(self.test_store.toy_shelf["C"])

    def test_successful_added_toy(self):
        result = self.test_store.add_toy("E", "Phone")

        self.assertEqual("Phone", self.test_store.toy_shelf["E"])
        self.assertEqual("Toy:Phone placed successfully!", result)

    def test_remove_toy_from_invalid_shelf_raise_ex(self):
        with self.assertRaises(Exception) as ex:
            self.test_store.remove_toy("??", "Mouse")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_toy_with_invalid_toy_raise_ex(self):
        self.test_store.toy_shelf["A"] = "Bear"
        with self.assertRaises(Exception) as ex:
            self.test_store.remove_toy("A", "Cat")

        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_remove_toy_successful(self):
        self.test_store.toy_shelf["A"] = "Bear"
        result = self.test_store.remove_toy("A", "Bear")

        self.assertIsNone(self.test_store.toy_shelf["A"])
        self.assertEqual("Remove toy:Bear successfully!", result)


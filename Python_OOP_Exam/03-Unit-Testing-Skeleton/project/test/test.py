from unittest import TestCase, main
from project.restaurant import Restaurant


class TestRestaurant(TestCase):

    def setUp(self) -> None:
        self.test_restaurant = Restaurant("Dinner", 100)

    def test_init(self):
        self.assertEqual("Dinner", self.test_restaurant.name)
        self.assertEqual(100, self.test_restaurant.capacity)
        self.assertEqual([], self.test_restaurant.waiters)

    def test_invalid_name_raise_VE(self):
        with self.assertRaises(ValueError) as ve:
            self.test_restaurant.name = ""

        self.assertEqual("Invalid name!", str(ve.exception))

    def test_invalid_capacity_raise_VE(self):
        with self.assertRaises(ValueError) as ve:
            self.test_restaurant.capacity = -1

        self.assertEqual("Invalid capacity!", str(ve.exception))

    def test_get_waiters(self):
        self.test_restaurant.waiters.append({'total_earnings': 10})
        self.test_restaurant.get_waiters(5, 20)
        self.assertEqual(1, len(self.test_restaurant.get_waiters()))

    def test_add_waiter_without_capacity(self):
        self.test_restaurant.capacity = 0
        result = self.test_restaurant.add_waiter("Ivan")

        self.assertEqual("No more places!", result)

    def test_add_waiter_with_exist_waiter(self):
        self.test_restaurant.waiters.append({"name": "Ivan"})

        result = self.test_restaurant.add_waiter("Ivan")

        self.assertEqual("The waiter Ivan already exists!", result)

    def test_add_waiter_new_waiter(self):
        result = self.test_restaurant.add_waiter("Petar")
        self.assertEqual(1, len(self.test_restaurant.waiters))
        self.assertEqual(f"The waiter Petar has been added.", result)

    def test_remove_waiter_with_invalid_name(self):
        result = self.test_restaurant.remove_waiter("Kiro")
        self.assertEqual("No waiter found with the name Kiro.", result)

    def test_remove_waiter_with_valid_name(self):
        self.test_restaurant.add_waiter("Trifon")
        result = self.test_restaurant.remove_waiter("Trifon")

        self.assertEqual(0, len(self.test_restaurant.waiters))
        self.assertEqual("The waiter Trifon has been removed.", result)

    def test_get_total_earnings(self):
        self.test_restaurant.waiters.append({'total_earnings': 10})

        self.assertEqual(10, self.test_restaurant.get_total_earnings())



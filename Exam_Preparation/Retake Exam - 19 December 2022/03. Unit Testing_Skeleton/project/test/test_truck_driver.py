from unittest import TestCase, main

from project.truck_driver import TruckDriver


class TestTruckDriver(TestCase):

    def setUp(self) -> None:
        self.test_truck = TruckDriver("Kamion", 10)

    def test_constructor_data(self):
        self.assertEqual("Kamion", self.test_truck.name)
        self.assertEqual(10, self.test_truck.money_per_mile)
        self.assertEqual({}, self.test_truck.available_cargos)
        self.assertEqual(0, self.test_truck.earned_money)
        self.assertEqual(0, self.test_truck.miles)

    def test_negative_earned_money_raise_VE(self):
        with self.assertRaises(ValueError) as ve:
            self.test_truck.earned_money = -5

        self.assertEqual(f"Kamion went bankrupt.", str(ve.exception))

    def test_successful_earned_money(self):
        self.test_truck.earned_money = 50

        self.assertEqual(50, self.test_truck.earned_money)

    def test_add_cargo_location_in_self_cargo_raise_exception(self):
        self.test_truck.available_cargos = {"Test": 10}

        with self.assertRaises(Exception) as ex:
            self.test_truck.add_cargo_offer("Test", 10)

        self.assertEqual("Cargo offer is already added.", str(ex.exception))

    def test_add_cargo_offer_successful_return_string(self):
        test_output = self.test_truck.add_cargo_offer("Test", 25)

        self.assertEqual(test_output, "Cargo for 25 to Test was added as an offer.")

    def test_drive_best_cargo_without_offer_raise_VE(self):
        result = self.test_truck.drive_best_cargo_offer()

        self.assertEqual("There are no offers available.", result)

    def test_drive_best_cargo_offer_successful(self):
        self.test_truck.add_cargo_offer("Pleven", 100)
        self.test_truck.add_cargo_offer("Montana", 500)
        best_offer = self.test_truck.drive_best_cargo_offer()

        expected = f"Kamion is driving 500 to Montana."

        self.assertEqual(expected, best_offer)
        self.assertEqual(4960, self.test_truck.earned_money)
        self.assertEqual(500, self.test_truck.miles)
        self.assertEqual(2, len(self.test_truck.available_cargos))

    def test_eat_miles_250(self):
        self.test_truck.add_cargo_offer("Petrich", 250)
        self.test_truck.drive_best_cargo_offer()

        self.assertEqual(2500 - 20, self.test_truck.earned_money)
        self.assertEqual(250, self.test_truck.miles)
        self.assertEqual(1, len(self.test_truck.available_cargos))

    def test_sleep_1000(self):
        self.test_truck.add_cargo_offer("Sofia", 1500)
        self.test_truck.drive_best_cargo_offer()

        calculated_earned_money = 15000 - ((1500 // 1000) * 45 + (1500 // 250) * 20) - 500

        self.assertEqual(calculated_earned_money, self.test_truck.earned_money)
        self.assertEqual(1500, self.test_truck.miles)
        self.assertEqual(1, len(self.test_truck.available_cargos))

    def test_pump_gas_1500(self):
        self.test_truck.add_cargo_offer("Veliko Tarnovo", 4500)
        self.test_truck.drive_best_cargo_offer()

        calculated_earned_money = 45000 - ((4500 // 1000) * 45 + (4500 // 250) * 20 + ((4500 // 1500) * 500))

        self.assertEqual(calculated_earned_money, self.test_truck.earned_money)
        self.assertEqual(4500, self.test_truck.miles)
        self.assertEqual(1, len(self.test_truck.available_cargos))

    def test_repair_truck_10000(self):
        self.test_truck.add_cargo_offer("Vratsa", 29_000)
        self.test_truck.drive_best_cargo_offer()

        calculated_earned_money = 290_000 - ((29_000 // 1000) * 45 + (29_000 // 250) * 20 +
                                             (29_000 // 1500) * 500 + ((29_000 // 10_000) * 7500))

        self.assertEqual(calculated_earned_money, self.test_truck.earned_money)
        self.assertEqual(29_000, self.test_truck.miles)
        self.assertEqual(1, len(self.test_truck.available_cargos))

    def test_repr_output(self):
        self.test_truck.name = "Ivan"
        self.test_truck.miles = 10_000
        self.assertEqual(f"Ivan has 10000 miles behind his back.", self.test_truck.__repr__())


if __name__ == "__main__":
    main()

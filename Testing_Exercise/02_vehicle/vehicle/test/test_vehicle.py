from project.vehicle import Vehicle
from unittest import TestCase, main

class TestVehicle(TestCase):

    def setUp(self) -> None:
        self.test_vehicle = Vehicle(50.0, 150.0)

    def test_init(self):
        self.assertEqual(50.0, self.test_vehicle.fuel)
        self.assertEqual(self.test_vehicle.fuel, self.test_vehicle.capacity)
        self.assertEqual(150.0, self.test_vehicle.horse_power)
        self.assertEqual(1.25, self.test_vehicle.fuel_consumption)

    def test_drive_without_needed_fuel_raise_error(self):
        with self.assertRaises(Exception) as ex:
            self.test_vehicle.drive(1000)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_with_enough_fuel(self):
        self.test_vehicle.fuel = 100
        self.test_vehicle.drive(10)
        left_fuel = 10 * 1.25

        self.assertEqual(100 - left_fuel, self.test_vehicle.fuel)

    def test_refuel_with_too_many_fuel(self):
        self.test_vehicle.capacity = 100
        with self.assertRaises(Exception) as ex:
            self.test_vehicle.refuel(101)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_successful(self):
        self.test_vehicle.fuel = 10
        self.test_vehicle.refuel(20)

        self.assertEqual(30, self.test_vehicle.fuel)

    def test_str_output(self):
        self.assertEqual("The vehicle has 150.0"
                         " horse power with 50.0 fuel left "
                         "and 1.25 fuel consumption", self.test_vehicle.__str__())
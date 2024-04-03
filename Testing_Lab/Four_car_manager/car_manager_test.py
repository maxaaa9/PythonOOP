from unittest import TestCase, main
from Four_car_manager.car_manager import Car


class TestCar(TestCase):

    def setUp(self) -> None:
        self.test_car = Car("Toyota", "Supra", 5, 150)

    def test_constructor_init(self):
        self.assertEqual("Toyota", self.test_car.make)
        self.assertEqual("Supra", self.test_car.model)
        self.assertEqual(5, self.test_car.fuel_consumption)
        self.assertEqual(150, self.test_car.fuel_capacity)
        self.assertEqual(0, self.test_car.fuel_amount)

    def test_make_null_exception_error(self):
        with self.assertRaises(Exception) as ex:
            self.test_car.make = ""

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_correct_make_method_successful_set_value(self):
        self.test_car.make("Karutsa")
        self.assertEqual("Karutsa", self.test_car.make)

    def test_raises_error_model_creation_check_setter(self):
        with self.assertRaises(Exception) as ex:
            self.test_car.model = ""

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_correct_model_creation(self):
        self.test_car.model = "Cupra"

        self.assertEqual("Cupra", self.test_car.model)

    def test_negative_fuel_consumption_raise_error(self):
        with self.assertRaises(Exception) as ex:
            self.test_car.fuel_consumption = -20

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_correct_set_fuel_consumption_to_car(self):
        self.test_car.fuel_consumption = 10

        self.assertEqual(10, self.test_car.fuel_consumption)

    def test_negative_fuel_capacity_raise_error(self):
        with self.assertRaises(Exception) as ex:
            self.test_car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_correct_capacity_set(self):
        self.test_car.fuel_capacity = 50

        self.assertEqual(50, self.test_car.fuel_capacity)

    def test_fuel_amount_with_negative_value_except_error(self):
        with self.assertRaises(Exception) as ex:
            self.test_car.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_correct_fuel_amount(self):
        self.test_car.fuel_amount = 500

        self.assertEqual(500, self.test_car.fuel_amount)

    def test_negative_refuel_set_up_except_error(self):
        with self.assertRaises(Exception) as ex:
            self.test_car.refuel(-1)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_correct_refuel(self):
        self.test_car.fuel_capacity = 500
        self.test_car.fuel_amount = 490
        self.test_car.refuel(500)

        self.assertEqual(500, self.test_car.fuel_amount)

    def test_drive_with_not_enough_fuel_except_error(self):
        self.test_car.fuel_consumption = 10000

        with self.assertRaises(Exception) as ex:
            self.test_car.drive(1000)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_with_enough_fuel_amount_decrease(self):
        self.test_car.fuel_capacity = 100
        self.test_car.fuel_consumption = 5
        self.test_car.fuel_amount = 60
        self.test_car.drive(25)
        test_needed_fuel = (25 / 100) * 5

        self.assertEqual(60 - test_needed_fuel, self.test_car.fuel_amount)


if __name__ == "__main__":
    main()

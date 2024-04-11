from project.second_hand_car import SecondHandCar
from unittest import TestCase, main


class TestSecondHandCar(TestCase):

    def setUp(self):
        self.car = SecondHandCar("Tesla",
                                 "Electrical",
                                 500,
                                 50_000)

    def test_init(self):
        self.assertEqual("Tesla", self.car.model)
        self.assertEqual("Electrical", self.car.car_type)
        self.assertEqual(500, self.car.mileage)
        self.assertEqual(50_000, self.car.price)
        self.assertEqual([], self.car.repairs)

    def test_price_raise_VE(self):
        with self.assertRaises(ValueError) as ve:
            self.car.price = 0

        self.assertEqual('Price should be greater than 1.0!', str(ve.exception))

    def test_mileage_raise_VE_as_value_less_than_100(self):
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 100

        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!',
                         str(ve.exception))

    def test_promotional_price_with_higher_new_price_raise_VE(self):
        self.car.price = 100
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(10000)

        self.assertEqual('You are supposed to decrease the price!', str(ve.exception))

    def test_set_new_correct_value(self):
        self.car.price = 200
        result = self.car.set_promotional_price(150)

        self.assertEqual(150, self.car.price)
        self.assertEqual(result, 'The promotional price has been successfully set.')

    def test_need_repair_expensive_price_return_impossible(self):
        self.car.price = 500
        result = self.car.need_repair(251, "brakes")

        self.assertEqual(result, 'Repair is impossible!')

    def test_repaired_car_increase_self_price_append_note(self):
        self.car.price = 500
        result = self.car.need_repair(100, "TestNote")

        self.assertEqual(600, self.car.price)
        self.assertEqual(1, len(self.car.repairs))
        self.assertEqual(result, f'Price has been increased due to repair charges.')

    def test_changed_greater_than_with_wrong_type(self):
        new_test_car = SecondHandCar("Honda", "Petrol", 500, 500)
        result = self.car.__gt__(new_test_car)

        self.assertEqual(result, 'Cars cannot be compared. Type mismatch!')

    def test_change_greater_than_with_valid_type(self):
        new_test_car = SecondHandCar("Honda", "Electrical", 500, 500)
        result = self.car.__gt__(new_test_car)

        self.assertTrue(result)

    def test_new_str_method_return_data(self):
        result = self.car.__str__()
        expect = f"""Model {self.car.model} | Type {self.car.car_type} | Milage {self.car.mileage}km
Current price: {self.car.price:.2f} | Number of Repairs: {len(self.car.repairs)}"""

        self.assertEqual(result, expect)
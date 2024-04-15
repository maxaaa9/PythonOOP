from project.robot import Robot
from unittest import TestCase, main


class TestRobot(TestCase):

    def setUp(self) -> None:
        self.test_robot = Robot("5", "Military", 100, 10_000)

        self.other_robot = Robot("3", "Education", 80, 8_000)

    def test_init(self):
        self.assertEqual("5", self.test_robot.robot_id)
        self.assertEqual("Military", self.test_robot.category)
        self.assertEqual(100, self.test_robot.available_capacity)
        self.assertEqual(10_000, self.test_robot.price)
        self.assertEqual([], self.test_robot.hardware_upgrades)
        self.assertEqual([], self.test_robot.software_updates)

    def test_invalid_category_raise_VE(self):
        with self.assertRaises(ValueError) as ve:
            self.test_robot.category = "None"

        self.assertEqual(f"Category should be one of "
                         f"'['Military', 'Education', 'Entertainment', 'Humanoids']'",
                         str(ve.exception))

    def test_price_with_negative_value_except_VE(self):
        with self.assertRaises(ValueError) as ve:
            self.test_robot.price = -1

        self.assertEqual("Price cannot be negative!", str(ve.exception))

    def test_upgrade_with_available_parts(self):
        self.test_robot.hardware_upgrades = ["Craps"]
        result = self.test_robot.upgrade("Craps", 10000)

        self.assertEqual(10_000, self.test_robot.price)
        self.assertEqual(1, len(self.test_robot.hardware_upgrades))
        self.assertEqual(f"Robot {self.test_robot.robot_id} was not upgraded.", result)

    def test_upgrade_robot_with_new_part(self):
        total_value = 2500 * 1.5 + 10_000
        result = self.test_robot.upgrade("Gun", 2500)

        self.assertEqual(1, len(self.test_robot.hardware_upgrades))
        self.assertEqual(total_value, self.test_robot.price)
        self.assertEqual(f'Robot {self.test_robot.robot_id} was '
                         f'upgraded with Gun.', result)

    def test_update_with_not_enough_capacity(self):
        result = self.test_robot.update(2.0, 10_000)

        self.assertEqual(f"Robot {self.test_robot.robot_id} was not updated.", result)

    def test_upgrade_with_less_version(self):
        self.test_robot.update(3.0, 10)
        result = self.test_robot.update(3.0, 10)

        self.assertEqual(f"Robot {self.test_robot.robot_id} was not updated.", result)

    def test_software_with_available_data(self):
        result = self.test_robot.update(3.1, 40)

        self.assertEqual(1, len(self.test_robot.software_updates))
        self.assertEqual(60, self.test_robot.available_capacity)
        self.assertEqual(f'Robot {self.test_robot.robot_id} was updated to version 3.1.', result)

    def test_greater_than(self):
        result = self.test_robot > self.other_robot
        self.assertEqual(result, f'Robot with ID {self.test_robot.robot_id} is '
                                 f'more expensive than Robot with ID {self.other_robot.robot_id}.')

    def test_is_equal_prices(self):
        self.test_robot.price = self.other_robot.price
        result = self.test_robot.__gt__(self.other_robot)

        self.assertEqual(f'Robot with ID {self.test_robot.robot_id} '
                         f'costs equal to Robot with ID {self.other_robot.robot_id}.', result)

    def test_less_than(self):
        self.other_robot.price = 99999999
        result = self.test_robot.__gt__(self.other_robot)

        self.assertEqual(f'Robot with ID {self.test_robot.robot_id} is '
                         f'cheaper than Robot with ID {self.other_robot.robot_id}.', result)


if __name__ == "__main__":
    main()

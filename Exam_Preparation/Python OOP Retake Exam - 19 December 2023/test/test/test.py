from project.climbing_robot import ClimbingRobot
from unittest import TestCase, main


class TestClimbingRobot(TestCase):

    def setUp(self) -> None:
        self.test_robot = ClimbingRobot("Alpine", "machine", 10, 10)
        self.test_robot_with_software = ClimbingRobot("Mountain", "climber", 10, 10)

        self.test_robot_with_software.installed_software = [{"name": 'main',
                                                             "memory_consumption": 3,
                                                             "capacity_consumption": 3},
                                                            {"name": 'backup',
                                                             "memory_consumption": 1,
                                                             "capacity_consumption": 1}]

    def test_init(self):
        self.assertEqual("Alpine", self.test_robot.category)
        self.assertEqual("machine", self.test_robot.part_type)
        self.assertEqual(10, self.test_robot.capacity)
        self.assertEqual(10, self.test_robot.memory)
        self.assertEqual([], self.test_robot.installed_software)
        self.assertEqual([{"name": 'main',
                           "memory_consumption": 3,
                           "capacity_consumption": 3},
                          {"name": 'backup',
                           "memory_consumption": 1,
                           "capacity_consumption": 1}], self.test_robot_with_software.installed_software)

    def test_category_setter_except_VE(self):
        with self.assertRaises(ValueError) as ve:
            self.test_robot.category = "None"

        self.assertEqual(f"Category should be one of {self.test_robot.ALLOWED_CATEGORIES}",
                         str(ve.exception))

    def test_category_with_correct_value(self):
        self.test_robot.category = "Mountain"

        self.assertEqual("Mountain", self.test_robot.category)
        self.assertEqual("Mountain", self.test_robot_with_software.category)

    def test_get_used_capacity(self):
        self.test_robot.installed_software = [{"name": "Test", "memory_consumption": 5, "capacity_consumption": 5},
                                              {"name": "Test2", "memory_consumption": 5, "capacity_consumption": 5}]

        self.assertEqual(10, self.test_robot.get_used_capacity())

    def test_available_capacity(self):
        self.test_robot.install_software({"name": "Macro",
                                          "memory_consumption": 6,
                                          "capacity_consumption": 10})

        self.assertEqual(0, self.test_robot.get_available_capacity())

    def test_get_used_memory(self):
        self.test_robot.installed_software = [{"name": "Test", "memory_consumption": 5, "capacity_consumption": 5},
                                              {"name": "Test2", "memory_consumption": 5, "capacity_consumption": 5}]

        self.assertEqual(10, self.test_robot.get_used_memory())

    def test_get_available_memory(self):
        self.test_robot.installed_software = [{"name": "Test", "memory_consumption": 5, "capacity_consumption": 5},
                                              {"name": "Test2", "memory_consumption": 5, "capacity_consumption": 5}]

        self.assertEqual(0, self.test_robot.get_available_memory())

    def test_installed_software_successful(self):
        result = self.test_robot.install_software({"name": "Macro",
                                                   "memory_consumption": 10,
                                                   "capacity_consumption": 10})

        self.assertEqual(1, len(self.test_robot.installed_software))
        self.assertEqual("Software 'Macro' successfully installed on Alpine part.", result)

    def test_installed_software_with_not_enough_memory(self):
        result = self.test_robot.install_software({"name": "Macro",
                                                   "memory_consumption": 40,
                                                   "capacity_consumption": 2})

        self.assertEqual("Software 'Macro' cannot be installed on Alpine part.", result)

    def test_installed_software_with_not_enough_capacity(self):
        result = self.test_robot.install_software({"name": "Macro",
                                                   "memory_consumption": 4,
                                                   "capacity_consumption": 20})

        self.assertEqual("Software 'Macro' cannot be installed on Alpine part.", result)


if __name__ == "__main__":
    main()

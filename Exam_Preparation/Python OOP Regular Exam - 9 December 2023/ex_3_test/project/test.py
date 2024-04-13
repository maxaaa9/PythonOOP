from unittest import TestCase, main
from collections import deque

from project.railway_station import RailwayStation


class TestRailwayStation(TestCase):

    def setUp(self):
        self.test_station = RailwayStation("Varna")

    def test_invalid_name_raise_VE(self):
        with self.assertRaises(ValueError) as ve:
            self.test_station.name = " "

        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

    def test_new_arrival_on_board_append_new_station(self):
        self.test_station.new_arrival_on_board("Burgas")

        self.assertEqual(1, len(self.test_station.arrival_trains))

    def test_train_has_arrived_with_diff_arrival_train(self):
        self.test_station.new_arrival_on_board("Tester")
        result = self.test_station.train_has_arrived("Other")

        self.assertEqual(result, "There are other trains to arrive before Other.")

    def test_train_has_arrived_with_same_train(self):
        self.test_station.new_arrival_on_board("Tester")
        result = self.test_station.train_has_arrived("Tester")

        self.assertEqual(0, len(self.test_station.arrival_trains))
        self.assertEqual(result, "Tester is on the platform and will leave in 5 minutes.")

    def test_train_has_left_except_True(self):
        self.test_station.new_arrival_on_board("Tester")
        self.test_station.train_has_arrived("Tester")
        result = self.test_station.train_has_left("Tester")

        self.assertEqual(0, len(self.test_station.departure_trains))
        self.assertTrue(result)

    def test_train_has_left_except_False(self):
        self.test_station.new_arrival_on_board("Tester1")
        self.test_station.train_has_arrived("Tester1")
        result = self.test_station.train_has_left("Tester")

        self.assertEqual(1, len(self.test_station.departure_trains))
        self.assertFalse(result)

        
if __name__ == "__main__":
    main()
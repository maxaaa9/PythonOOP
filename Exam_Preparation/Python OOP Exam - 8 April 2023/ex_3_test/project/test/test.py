from unittest import TestCase, main

from project.tennis_player import TennisPlayer


class TestTennisPlayer(TestCase):

    def setUp(self) -> None:
        self.test_player = TennisPlayer("Ivan", 20, 200.0)

        self.other_player = TennisPlayer("Test", 20, 100.0)

    def test_init(self):
        self.assertEqual("Ivan", self.test_player.name)
        self.assertEqual(20, self.test_player.age)
        self.assertEqual(200.0, self.test_player.points)
        self.assertEqual([], self.test_player.wins)

    def test_invalid_name_len_raise_VE(self):
        with self.assertRaises(ValueError) as ve:
            self.test_player.name = "NO"

        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_invalid_age_raise_VE(self):
        with self.assertRaises(ValueError) as ve:
            self.test_player.age = 17

        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))

    def test_add_new_win_with_new_win(self):
        self.test_player.add_new_win("WEFA")

        self.assertEqual(1, len(self.test_player.wins))

    def test_add_new_win_with_same_tournament(self):
        self.test_player.wins.append("Tester")
        result = self.test_player.add_new_win("Tester")

        self.assertEqual("Tester has been already added to the list of wins!", result)

    def test_test_player_less_than_other_player(self):
        self.other_player.points = 200.1
        result = self.test_player.__lt__(self.other_player)

        self.assertEqual('Test is a top seeded player and he/she is better than Ivan', result)

    def test_test_player_with_higher_than_other_player(self):
        result = self.test_player.__lt__(self.other_player)

        self.assertEqual(f'Ivan is a better player than Test', result)

    def test_str_method(self):
        self.test_player.wins = ["Test1", "Test2"]
        expect = f"Tennis Player: Ivan\n" \
                 f"Age: 20\n" \
                 f"Points: 200.0\n" \
                 f"Tournaments won: Test1, Test2"

        self.assertEqual(expect, str(self.test_player))


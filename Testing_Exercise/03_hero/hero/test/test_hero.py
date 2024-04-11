from unittest import TestCase, main
from project.hero import Hero


class TestHero(TestCase):

    def setUp(self) -> None:
        self.test_hero = Hero("Madness", 200, 2000.0, 10000.0)

    def test_init(self):
        self.assertEqual("Madness", self.test_hero.username)
        self.assertEqual(200, self.test_hero.level)
        self.assertEqual(2000.0, self.test_hero.health)
        self.assertEqual(10000.0, self.test_hero.damage)

    def test_battle_same_username(self):
        enemy_hero = Hero("Madness", 200, 2000.0, 100.0)

        with self.assertRaises(Exception) as ex:
            self.test_hero.battle(enemy_hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_without_health(self):
        enemy_hero = Hero("Ivan", 200, 2000.0, 100.0)
        self.test_hero.health = -1

        with self.assertRaises(ValueError) as ve:
            self.test_hero.battle(enemy_hero)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_battle_with_negative_health_enemy(self):
        enemy_hero = Hero("Ivan", 200, -5, 100.0)

        with self.assertRaises(ValueError) as ve:
            self.test_hero.battle(enemy_hero)

        self.assertEqual(f"You cannot fight {enemy_hero.username}. He needs to rest", str(ve.exception))

    def test_battle_both_sides_without_health(self):
        self.test_hero.damage = 10
        self.test_hero.health = 10
        enemy_hero = Hero("Ivan", 200, 10.0, 10.0)

        result = self.test_hero.battle(enemy_hero)

        self.assertEqual("Draw", result)

    def test_battle_you_win(self):
        self.test_hero.damage = 100
        self.test_hero.health = 100
        enemy_hero = Hero("Ivan", 1, 5.0, 10.0)

        result = self.test_hero.battle(enemy_hero)

        self.assertEqual(201, self.test_hero.level)
        self.assertEqual(95.0, self.test_hero.health)
        self.assertEqual(105.0, self.test_hero.damage)
        self.assertEqual("You win", result)

    def test_battle_you_lose(self):
        self.test_hero.damage = 0
        self.test_hero.health = 100
        enemy_hero = Hero("Ivan", 1, 5.0, 10.0)

        result = self.test_hero.battle(enemy_hero)

        self.assertEqual(2, enemy_hero.level)
        self.assertEqual(10.0, enemy_hero.health)
        self.assertEqual(15.0, enemy_hero.damage)
        self.assertEqual("You lose", result)

    def test_str(self):
        self.assertEqual(f"Hero Madness: 200 lvl\nHealth: 2000.0\nDamage: 10000.0\n", self.test_hero.__str__())
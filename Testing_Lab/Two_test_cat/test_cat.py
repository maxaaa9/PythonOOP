from unittest import TestCase, main
from Two_test_cat.cat import Cat


class CatTests(TestCase):

    def setUp(self) -> None:
        self.test_cat = Cat("Muri")

    def test_correct_init(self):
        self.assertEqual("Muri", self.test_cat.name)
        self.assertFalse(self.test_cat.fed)
        self.assertFalse(self.test_cat.sleepy)
        self.assertEqual(0, self.test_cat.size)

    def test_increase_size_of_cat_after_eating(self):
        test_size = self.test_cat.size + 1
        self.test_cat.eat()

        self.assertEqual(test_size, self.test_cat.size)

    def test_fed_cat_after_eating(self):
        self.test_cat.eat()
        self.assertEqual(True, self.test_cat.fed)

    def test_fed_cat_raise_error(self):
        self.test_cat.fed = True
        with self.assertRaises(Exception) as ex:
            self.test_cat.eat()

        self.assertEqual('Already fed.', str(ex.exception))

    def test_cat_cannot_fall_a_sleep_if_not_fed(self):
        self.test_cat.fed = False
        with self.assertRaises(Exception) as ex:
            self.test_cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_cat_cannot_sleep_after_sleeping(self):
        self.test_cat.fed = True
        self.test_cat.sleepy = True

        self.test_cat.sleep()

        self.assertFalse(self.test_cat.sleepy)


if __name__ == "__main__":
    main()

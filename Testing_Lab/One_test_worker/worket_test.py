from unittest import TestCase, main
from One_test_worker.worker import Worker


class WorkerTests(TestCase):

    def setUp(self) -> None:
        self.worker = Worker("Ivan",
                             2000,
                             300,)

    def test_correct_init_test(self):
        self.assertEqual("Ivan", self.worker.name)
        self.assertEqual(2000, self.worker.salary)
        self.assertEqual(300, self.worker.energy)

    def test_correct_work_energy_decrease(self):
        test_number = 5
        test_energy_increment = self.worker.energy + test_number
        for energy in range(test_number):
            self.worker.rest()

        self.assertEqual(test_energy_increment, self.worker.energy)

    def test_correct_money_increase(self):
        test_money = self.worker.salary * 5
        for salary in range(5):
            self.worker.work()

        self.assertEqual(test_money, self.worker.money)

    def test_negative_or_equal_energy_raise_exception_error(self):
        self.worker.energy = -1
        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_correct_energy_decrease_after_work_method_is_called(self):
        test_energy_decrease = self.worker.energy - 5
        for test in range(5):
            self.worker.work()

        self.assertEqual(test_energy_decrease, self.worker.energy)

    def test_get_info_proper_return(self):
        test_string = f'Ivan has saved 0 money.'

        self.assertEqual(test_string, self.worker.get_info())


if __name__ == "__main__":
    main()

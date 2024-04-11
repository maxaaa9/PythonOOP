from unittest import TestCase, main
from Three_list.extended_list import IntegerList


class TestList(TestCase):

    def setUp(self) -> None:
        self.test_list = IntegerList(1, 2, 3, 4, 5.6, "Trash")

    def test_init(self):
        test_data = [1, 2, 3, 4]
        self.assertEqual(test_data, self.test_list.get_data())

    def test_add_operation_return_list(self):
        test_element = 5
        self.test_list.add(test_element)

        self.assertEqual([1, 2, 3, 4, 5], self.test_list.get_data())

    def test_add_operation_throw_val_error_if_not_int(self):
        with self.assertRaises(ValueError) as ve:
            self.test_list.add("One")

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_remove_index_throw_idx_error_if_out_of_range(self):
        with self.assertRaises(IndexError) as ie:
            self.test_list.remove_index(len(self.test_list.get_data()))

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_remove_successful(self):
        test_list = [1, 2, 4]
        self.test_list.remove_index(2)

        self.assertEqual(test_list, self.test_list.get_data())

    def test_get_successful_taken_item(self):
        test_index = 2

        self.assertEqual(3, self.test_list.get(test_index))

    def test_get_method_throw_idx_error_if_out_of_range(self):
        with self.assertRaises(IndexError) as ie:
            self.test_list.get(len(self.test_list.get_data()))

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_valid_insert(self):
        test_list = [10] + self.test_list.get_data()
        self.test_list.insert(0, 10)

        self.assertEqual(test_list, self.test_list.get_data())

    def test_insert_method_throw_idx_error(self):
        invalid_index = len(self.test_list.get_data())
        with self.assertRaises(IndexError) as ie:
            self.test_list.insert(invalid_index, 1)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_method_throw_value_error(self):
        test_element = "Zero"
        with self.assertRaises(ValueError) as ve:
            self.test_list.insert(0, test_element)

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_get_biggest_num(self):
        max_int = max(self.test_list.get_data())

        self.assertEqual(max_int, self.test_list.get_biggest())

    def test_get_index_from_list(self):
        test_element = 2

        self.assertEqual(1, self.test_list.get_index(test_element))


if __name__ == "__main__":
    main()

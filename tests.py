import unittest
from test_task import return_unique_list, return_list_of_prime_numbers, sorted_list_by_string
from point import Point


class CheckTask(unittest.TestCase):

    def setUp(self):
        self.point = Point(0, 0)
        self.strings = ['1', '32434ww', '233', '2222', '45345435656456', '4432asd', '36546awd', '23']
        self.result_1 = ['1', '23', '233', '2222', '32434ww', '4432asd', '36546awd', '45345435656456']
        self.result_2 = ['45345435656456', '36546awd', '32434ww', '4432asd', '2222', '233', '23', '1']
        self.distance = 0

    def test_return_unique_list(self):
        my_list = [1, 1, 1, 1, 6, 6, 6, 6, 6, 9, 9, 9, 5, 5, 5, 5]
        unique_list = return_unique_list(my_list)
        self.assertEqual(unique_list, [1, 5, 6, 9])

    def test_return_list_of_prime_numbers(self):
        prime_numbers = return_list_of_prime_numbers(-100, 25)
        self.assertEqual(prime_numbers, [3, 5, 7, 11, 13, 17, 19, 23])

    def test_sorted_list_by_string(self):
        sorted_list = sorted_list_by_string(self.strings, False)
        self.assertEqual(sorted_list, self.result_1)

    def test_sorted_list_by_string_reverse(self):
        sorted_list = sorted_list_by_string(self.strings, True)
        self.assertEqual(sorted_list, self.result_2)

    def test_get_point_coordinates(self):
        self.assertEqual(self.point.get_coord(), (0, 0))

    def test_set_point_coordinates(self):
        self.point.set_coord(10, 10)
        self.assertEqual(self.point.get_coord(), (10, 10))

    def test_distance_to_another_point(self):
        self.point.distance_to_the_another_point(3, 4)
        self.assertEqual(self.point.distance, 5)


if __name__ == "__main__":
    unittest.main()

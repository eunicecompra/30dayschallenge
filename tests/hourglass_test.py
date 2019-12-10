import unittest

from python3_implementation import hourglass

class Hourglass(unittest.TestCase):

    def test_find_max_sum_hourglass(self):
        array = [
            [1, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0],
            [0, 0, 2, 4, 4, 0],
            [0, 0, 0, 2, 0, 0],
            [0, 0, 1, 2, 4, 0]
        ]
        max_sum = hourglass.find_max_sum_hourglass(array)
        self.assertEqual(19, max_sum)

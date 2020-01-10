import unittest

from unittest.mock import patch
from src import hourglass

class Hourglass(unittest.TestCase):
    test_data1 = [
        "1 1 1 0 0 0",
        "0 1 0 0 0 0",
        "1 1 1 0 0 0",
        "0 0 2 4 4 0",
        "0 0 0 2 0 0",
        "0 0 1 2 4 0"
    ]
    test_data2 = [
        "-1 1 -1 0 0 0",
        "0 -1 0 0 0 0",
        "-1 -1 -1 0 0 0",
        "0 -9 2 -4 -4 0",
        "-7 0 0 -2 0 0",
        "0 0 -1 -2 -4 0"
    ]

    @patch("builtins.input", side_effect=test_data1)
    def test_find_max_sum_hourglass(self, test_data):
        max_sum = hourglass.main()
        self.assertEqual(19, max_sum)

    @patch("builtins.input", side_effect=test_data2)
    def test_find_max_sum_hourglass_2(self, test_data):
        max_sum = hourglass.main()
        self.assertEqual(0, max_sum)
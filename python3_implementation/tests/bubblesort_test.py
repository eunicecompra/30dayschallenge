import unittest

from unittest.mock import patch
from src import bubblesort

class BubbleSortTest(unittest.TestCase):
    @patch("builtins.input", side_effect=["3","3 2 1"])
    def test_bubble_sort(self, test_data):
        s = bubblesort.main()
        self.assertListEqual(s.sorted_array, [1,2,3])
        self.assertEqual(s.swap_cnt, 3)
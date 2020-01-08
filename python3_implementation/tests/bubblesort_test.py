import unittest

from src import bubblesort

class BubbleSortTest(unittest.TestCase):
    def test_bubble_sort(self):
        sorted_list = bubblesort.do_bubble_sort(3, [3,2,1])
        self.assertListEqual(sorted_list, [1,2,3])
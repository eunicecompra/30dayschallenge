import unittest

from src.bubblesort import BubbleSort

class BubbleSortTest(unittest.TestCase):
    def test_bubble_sort(self):
        b = BubbleSort()
        sorted_list = b.do_bubble_sort(3, [3,2,1])
        self.assertListEqual(sorted_list, [1,2,3])
        self.assertEqual(b.swap_cnt, 3)
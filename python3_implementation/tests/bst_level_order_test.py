import unittest

from unittest.mock import patch
from src import bst_level_order

class BSTLevelOrderTest(unittest.TestCase):
    test_data = [6,3,5,4,7,2,1]

    @patch("builtins.input", side_effect=test_data)
    def testLevelOrder(self, test_data):
        order = bst_level_order.main()
        self.assertListEqual(order, [3,2,5,1,4,7])
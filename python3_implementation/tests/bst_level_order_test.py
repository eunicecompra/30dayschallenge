import unittest

from src.bst_level_order import Solution

class BSTLevelOrderTest(unittest.TestCase):
    def testLevelOrder(self):
        tree_elements = [3,5,4,7,2,1]
        root = None
        s = Solution()
        for i in tree_elements:
            root = s.insert(root,i)
        order = s.levelOrder(root)
        self.assertListEqual(order, [3,2,5,1,4,7])
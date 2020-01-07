import unittest

from src.queues_stacks import Solution

class Queues_Stacks(unittest.TestCase):

    def test_pushCharacter(self):
        s = Solution()
        s.pushCharacter('s')
        s.pushCharacter('t')
        self.assertListEqual(s.string_stack, ['s','t'])

    def test_enqueueCharacter(self):
        s = Solution()
        s.enqueueCharacter('s')

    def test_popCharacter(self):
        s = Solution()
        s.popCharacter()

    def test_dequeueCharacter(self):
        s = Solution()
        s.dequeueCharacter()
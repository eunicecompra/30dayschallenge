import unittest

from collections import deque
from src.queues_stacks import Solution

class Queues_Stacks(unittest.TestCase):

    def test_pushCharacter(self):
        s = Solution()
        s.pushCharacter('s')
        s.pushCharacter('t')
        self.assertListEqual(s.string_stack, ['s','t'])

    def test_enqueueCharacter(self):
        s = Solution()
        s.enqueueCharacter('r')
        self.assertListEqual(list(s.string_queue), ['r'])

    def test_popCharacter(self):
        s = Solution()
        s.pushCharacter('s')
        s.pushCharacter('t')
        s.pushCharacter('a')
        s.pushCharacter('r')
        self.assertEqual(s.popCharacter(), 'r')
        self.assertListEqual(s.string_stack, ['s','t','a'])

    def test_dequeueCharacter(self):
        s = Solution()
        s.enqueueCharacter('s')
        s.enqueueCharacter('t')
        s.enqueueCharacter('a')
        s.enqueueCharacter('r')
        self.assertEqual(s.dequeueCharacter(), 's')
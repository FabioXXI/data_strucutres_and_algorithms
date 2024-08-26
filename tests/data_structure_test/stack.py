from typing import NoReturn
from data_structure.stack import Stack
from unittest import TestCase

class StackTest(TestCase):
    def test_append_and_pop_and_to_list(self) -> NoReturn:
        stack = Stack()
        stack.append(10)
        stack.append(20)
        stack.append(30)
        self.assertEqual(stack.to_list(), [30, 20, 10])
        self.assertEqual(stack.pop(), 30)
        self.assertEqual(stack.pop(), 20)
        self.assertEqual(stack.pop(), 10)

    def test_size(self) -> NoReturn:
        stack = Stack()
        stack.append(10)
        stack.append(20)
        self.assertEqual(stack.get_size(), 2)
        stack.pop()
        self.assertEqual(stack.get_size(), 1)
        stack.pop()
        self.assertEqual(stack.get_size(), 0)
        stack.append(10)
        self.assertEqual(stack.get_size(), 1)
        self.assertEqual(stack.pop(), 10)
        self.assertEqual(stack.get_size(), 0)

if __name__ == "__main__":
    StackTest()
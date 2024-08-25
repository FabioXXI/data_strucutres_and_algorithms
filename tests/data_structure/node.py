import unittest
from typing import NoReturn
from data_structure.node import Node

class NodeTest(unittest.TestCase):
    def test_value(self) -> NoReturn:
        node = Node(10)
        self.assertEqual(node.get_value(), 10)

    def test_next(self) -> NoReturn:
        n1 = Node(10)
        n2 = Node(20)
        n1.put_next(n2)
        self.assertEqual(n1.get_next(), n2)

    def test_prev(self) -> NoReturn:
        n1 = Node(10)
        n2 = Node(20)
        n2.put_prev(n1)
        self.assertEqual(n1, n2.get_prev())

    def test_copy(self) -> NoReturn:
        node = Node(10)
        n1 = node.get_copy(deepcp=False)
        n2 = node.get_copy()
        self.assertEqual(n1, node)
        self.assertNotEqual(n2, node)

if __name__ == "__main__":
    NodeTest()
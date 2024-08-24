import unittest
from algorithms.node import Node
from typing import NoReturn


class NodeTest(unittest.TestCase):
    def test_value(self) -> NoReturn:
        node = Node(10)
        self.assertEqual(node.get_value(), 10)

    def test_point_to(self) -> NoReturn:
        n1 = Node(10)
        n2 = Node(20)
        n1.put_point_to(n2)
        self.assertEqual(n1.get_point_to(), n2)

    def test_pointed_from(self) -> NoReturn:
        n1 = Node(10)
        n2 = Node(20)
        n1.put_pointed_from(n2)
        self.assertEqual(n1.get_pointed_from(), n2)

    def test_append_point_to(self) -> NoReturn:
        nodes = [Node(10) for _ in range(10)]
        node = Node(20)
        for n in nodes:
            node.append_point_to(n)
        self.assertEqual(node.get_point_to(), nodes)

    def test_append_pointed_from(self) -> NoReturn:
        nodes = [Node(10) for _ in range(10)]
        node = Node(20)
        for n in nodes:
            node.append_pointed_from(n)
        self.assertEqual(node.get_pointed_from(), nodes)

    def test_pop_point_to(self) -> NoReturn:
        nodes = [Node(10) for _ in range(10)]
        node = Node(20)
        for n in nodes:
            node.append_point_to(n)
        self.assertEqual(node.pop_point_to(), nodes[-1])

    def test_pop_pointed_from(self) -> NoReturn:
        nodes = [Node(10) for _ in range(10)]
        node = Node(20)
        for n in nodes:
            node.append_pointed_from(n)
        self.assertEqual(node.pop_pointed_from(), nodes[-1])


if __name__ == "__main__":
    NodeTest()
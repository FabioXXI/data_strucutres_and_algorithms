from data_structure.heap_node import HeapNode
from unittest import TestCase
from typing import NoReturn

class HeapNodeTest(TestCase):
    def test_value(self) -> NoReturn:
        node = HeapNode(10)
        self.assertEqual(10, node.get_value())

    def test_prev(self) -> NoReturn:
        n1 = HeapNode(10)
        n2 = HeapNode(20)
        n2.put_prev(n1)
        self.assertEqual(n2.get_prev(), n1)

    def test_left_and_right(self) -> NoReturn:
        n1 = HeapNode(10)
        n2 = HeapNode(20)
        n3 = HeapNode(30)
        n1.put_left(n2)
        n1.put_right(n3)
        self.assertEqual(n1.get_left(), n2)
        self.assertEqual(n1.get_right(), n3)

    def test_clean_node(self) -> NoReturn:
        node = HeapNode(10)
        n1 = HeapNode(10)
        n2 = HeapNode(20)
        n3 = HeapNode(30)
        node.put_right(n1)
        node.put_left(n2)
        node.put_prev(n3)
        node.clean_node()
        self.assertEqual(node.get_right(), None)
        self.assertEqual(node.get_left(), None)
        self.assertEqual(node.get_prev(), None)
        self.assertEqual(node.get_value(), None)

if __name__ == "__main__":
    HeapNodeTest()
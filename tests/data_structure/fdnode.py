import unittest
from data_structure.fdnode import FDNode
from typing import NoReturn

class FDNodeTest(unittest.TestCase):
    def test_value(self) -> NoReturn:
        node = FDNode(10)
        self.assertEqual(node.get_value(), 10)

    def test_pointers(self) -> NoReturn:
        n1 = FDNode(10)
        n2 = FDNode(20)
        n3 = FDNode(30)
        n4 = FDNode(40)
        n5 = FDNode(50)
        n1.put_up(n2)
        n1.put_right(n3)
        n1.put_down(n4)
        n1.put_left(n5)
        self.assertEqual(n1.get_up(), n2)
        self.assertEqual(n1.get_right(), n3)
        self.assertEqual(n1.get_down(), n4)
        self.assertEqual(n1.get_left(), n5)

    def test_clean(self) -> NoReturn:
        n1 = FDNode(10)
        n2 = FDNode(20)
        n3 = FDNode(30)
        n4 = FDNode(40)
        n5 = FDNode(50)
        n1.put_up(n2)
        n1.put_right(n3)
        n1.put_down(n4)
        n1.put_left(n5)
        n1.clean_node()
        self.assertEqual(n1.get_left(), None)
        self.assertEqual(n1.get_up(), None)
        self.assertEqual(n1.get_down(), None)
        self.assertEqual(n1.get_up(), None)
        self.assertEqual(n1.get_value(), None)

    def test_copy(self) -> NoReturn:
        node = FDNode(10)
        n1 = node.get_copy(deepcp=False)
        n2 = node.get_copy()
        self.assertEqual(n1, node)
        self.assertNotEqual(n2, node)

if __name__ == "__main__":
    FDNodeTest()
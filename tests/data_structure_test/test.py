from tests.data_structure_test.fdnode import FDNodeTest
from tests.data_structure_test.node import NodeTest
from tests.data_structure_test.multidimensional_node import MultidimensionalNodeTest
from typing import NoReturn
import unittest

class DataStructureTest(unittest.TestCase):
    def __init__(self) -> NoReturn:
        FDNodeTest()
        NodeTest()
        MultidimensionalNodeTest()

if __name__ == "__main__":
    DataStructureTest()
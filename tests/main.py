from typing import NoReturn
import unittest
from tests.data_structure_test.test import DataStructureTest
from tests.data_structure_test.fdnode import FDNodeTest
from tests.data_structure_test.node import NodeTest
from tests.data_structure_test.multidimensional_node import MultidimensionalNodeTest

class Test(unittest.TestCase):
    def __init__(self) -> NoReturn:
        DataStructureTest()

if __name__ == "__main__":
    Test()
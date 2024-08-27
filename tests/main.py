from typing import NoReturn
import unittest
from tests.data_structure_test.test import DataStructureTest
from tests.data_structure_test.fdnode import FDNodeTest
from tests.data_structure_test.node import NodeTest
from tests.data_structure_test.multidimensional_node import MultidimensionalNodeTest
from tests.data_structure_test.stack import StackTest
from tests.data_structure_test.queue import QueueTest
from tests.data_structure_test.heap_node import HeapNodeTest

class Test(unittest.TestCase):
    def __init__(self) -> NoReturn:
        DataStructureTest()

if __name__ == "__main__":
    Test()
from unittest import TestCase
from typing import NoReturn
from data_structure.queue import Queue

class QueueTest(TestCase):
    def test_append_and_pop_and_size_and_to_list(self) -> NoReturn:
        queue = Queue()
        queue.append(10)
        queue.append(20)
        queue.append(30)
        self.assertEqual(queue.get_size(), 3)
        self.assertEqual(queue.pop_from_front(), 10)
        self.assertEqual(queue.get_size(), 2)
        self.assertEqual(queue.pop_from_front(), 20)
        self.assertEqual(queue.get_size(), 1)
        self.assertEqual(queue.pop_from_front(), 30)
        self.assertEqual(queue.get_size(), 0)
        queue.append(10)
        queue.append(20)
        queue.append(30)
        self.assertEqual(queue.to_list(), [10, 20, 30])
        self.assertEqual(queue.get_size(), 3)
        self.assertEqual(queue.pop_from_end(), 30)
        self.assertEqual(queue.get_size(), 2)
        self.assertEqual(queue.pop_from_end(), 20)
        self.assertEqual(queue.get_size(), 1)
        self.assertEqual(queue.pop_from_end(), 10)
        self.assertEqual(queue.get_size(), 0)

if __name__ == "__main__":
    QueueTest()
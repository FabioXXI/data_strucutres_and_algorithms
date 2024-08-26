from data_structure.node import Node
from typing import Any, NoReturn

class Queue:
    total_instances = 0
    total_active_queues = 0

    @classmethod
    def increase_total_instances(cls) -> NoReturn:
        cls.total_instances += 1

    @classmethod
    def increase_total_active_queues(cls) -> NoReturn:
        cls.total_active_queues += 1

    @classmethod
    def decrease_total_active_queues(cls) -> NoReturn:
        cls.total_active_queues -= 1

    @classmethod
    def get_total_instances(cls) -> int:
        return cls.total_instances

    @classmethod
    def get_total_active_queues(cls) -> int:
        return cls.total_active_queues

    def __init__(self) -> NoReturn:
        self.first = None
        self.last = None
        self.size = 0
        Queue.increase_total_active_queues()
        Queue.increase_total_instances()

    def get_first(self) -> Node:
        return self.first

    def put_first(self, node: Node) -> NoReturn:
        self.first = node

    def get_last(self) -> Node:
        return self.last

    def put_last(self, node: Node) -> NoReturn:
        self.last = node

    def get_size(self) -> int:
        return self.size

    def increase_size(self) -> NoReturn:
        self.size += 1

    def decrease_size(self) -> NoReturn:
        self.size -= 1

    def reset_size(self) -> NoReturn:
        self.size = 0

    def append(self, value: Any) -> NoReturn:
        node = Node(value)
        self.increase_size()
        if not(self.get_first()):
            self.put_first(node)
            self.put_last(self.get_first())
            return
        self.get_last().put_next(node)
        node.put_prev(self.get_last())
        self.put_last(node)

    def to_list(self) -> list[Any]:
        l = []
        node = self.get_first()
        while node:
            l.append(node.get_value())
            node = node.get_next()
        return l

    def pop_from_end(self) -> Any:
        if not(self.get_first()):
            raise "Not value available to be popped"
        value = self.get_last().get_value()
        self.decrease_size()
        if self.is_first_equal_last():
            self.del_first_and_last()
            return value
        self.put_last(self.get_last().get_prev())
        self.get_last().del_next()
        return value

    def pop_from_front(self) -> Any:
        if not(self.get_first()):
            raise "Not value available to be popped"
        value = self.get_first().get_value()
        self.decrease_size()
        if self.is_first_equal_last():
            self.del_first_and_last()
            return value
        self.put_first(self.get_first().get_next())
        self.get_first().del_prev()
        return value

    def del_first_and_last(self) -> NoReturn:
        self.del_first()
        self.del_last()

    def del_first(self) -> NoReturn:
        self.first = None

    def del_last(self) -> NoReturn:
        self.last = None

    def is_first_equal_last(self) -> bool:
        return self.get_first() == self.get_last()

    def __len__(self) -> int:
        return self.get_size()

    def __repr__(self) -> str:
        return f"Queue()"

    def __del__(self) -> NoReturn:
        self.del_first_and_last()
        Queue.decrease_total_active_queues()
from typing import NoReturn, Any
from data_structure.node import Node

class Stack:
    total_instances = 0
    total_active_stacks = 0

    @classmethod
    def increase_total_instances(cls) -> NoReturn:
        cls.total_instances += 1

    @classmethod
    def increase_total_active_stacks(cls) -> NoReturn:
        cls.total_active_stacks += 1

    @classmethod
    def decrease_total_active_stacks(cls) -> NoReturn:
        cls.total_active_stacks -= 1

    @classmethod
    def get_total_instances(cls) -> int:
        return cls.total_instances

    @classmethod
    def get_total_active_stacks(cls) -> int:
        return cls.total_active_stacks

    def __init__(self) -> NoReturn:
        self.first = None
        self.last = None
        self.size = 0
        Stack.increase_total_active_stacks()
        Stack.increase_total_instances()

    def get_first(self) -> Node:
        return self.first

    def get_last(self) -> Node:
        return self.last

    def put_first(self, node: Node) -> NoReturn:
        self.first = node

    def put_last(self, node: Node) -> NoReturn:
        self.last = node

    def increase_size(self) -> NoReturn:
        self.size += 1

    def decrease_size(self) -> NoReturn:
        self.size -= 1

    def get_size(self) -> int:
        return self.size

    def to_list(self) -> list:
        l = []
        node = self.first
        while node:
            l.append(node.get_value())
            node = node.get_next()
        return l

    def append(self, value: Any) -> NoReturn:
        node = Node(value)
        self.increase_size()
        if not(self.get_first()):
            self.put_first(node)
            self.put_last(self.get_first())
            return
        if self.is_first_equal_last():
            self.put_first(node)
            self.get_first().put_next(self.get_last())
            return
        node.put_next(self.get_first())
        self.put_first(node)

    def pop(self) -> Any:
        if not(self.get_first()):
            raise "Not value available to be popped"
        value = self.get_first().get_value()
        self.decrease_size()
        if self.is_first_equal_last():
            self.del_first_and_last()
            return value
        node = self.get_first()
        self.put_first(node.get_next())
        node.clean_node()
        return value

    def del_first(self) -> NoReturn:
        self.get_first().clean_node()
        self.put_first(None)

    def del_last(self) -> NoReturn:
        self.get_last().clean_node()
        self.put_last(None)

    def del_first_and_last(self) -> NoReturn:
        self.del_first()
        self.del_last()

    def reset_size(self) -> NoReturn:
        self.size = 0

    def is_first_equal_last(self) -> bool:
        return self.get_first() == self.get_last()

    def __len__(self) -> int:
        return self.get_size()

    def __del__(self) -> NoReturn:
        self.put_first(None)
        self.put_last(None)
        self.reset_size()
        Stack.decrease_total_active_stacks()

    def __repr__(self) -> str:
        return f"Stack()"
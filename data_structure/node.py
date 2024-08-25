from typing import NoReturn, Any, Optional

class Node:
    total_instances = 0
    total_active_nodes = 0

    @classmethod
    def increase_total_instances(cls) -> NoReturn:
        cls.total_instances += 1

    @classmethod
    def increase_total_active(cls) -> NoReturn:
        cls.total_active_nodes += 1

    @classmethod
    def decrease_total_active(cls) -> NoReturn:
        cls.total_active_nodes -= 1

    @classmethod
    def get_total_instances(cls) -> int:
        return cls.total_instances

    @classmethod
    def get_total_active_nodes(cls) -> int:
        return cls.total_active_nodes

    def __init__(self, value: Any, next: Optional['Node'], prev: Optional['Node']) -> NoReturn:
        self.value = value
        self.next = next
        self.prev = prev
        Node.increase_total_active()
        Node.increase_total_instances()

    def put_value(self, value: Any) -> NoReturn:
        self.value = value

    def put_next(self, next: Optional['Node']) -> NoReturn:
        self.next = next

    def put_prev(self, prev: Optional['Node']) -> NoReturn:
        self.prev = prev

    def get_value(self) -> Any:
        return self.value

    def get_next(self) -> Optional['Node']:
        return self.next

    def get_prev(self) -> Optional['Node']:
        return self.prev

    def del_value(self) -> NoReturn:
        self.put_value(None)

    def del_next(self) -> NoReturn:
        self.put_next(None)

    def del_prev(self) -> NoReturn:
        self.put_prev(None)

    def del_next_and_prev(self) -> NoReturn:
        self.del_next()
        self.del_next()

    def clean_node(self) -> NoReturn:
        self.del_next_and_prev()
        self.del_value()

    def __del__(self) -> NoReturn:
        self.clean_node()
        Node.decrease_total_active()

    def __repr__(self) -> str:
        return f"Node({self.get_value()!r}, {self.get_next()!r}, {self.get_prev()!r})"
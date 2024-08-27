from typing import NoReturn, Any, Optional

class HeapNode:
    total_instances = 0
    total_active_heap_node = 0

    @classmethod
    def get_total_instances(cls) -> int:
        return cls.total_instances

    @classmethod
    def get_total_active_heap_node(cls) -> int:
        return cls.total_active_heap_node

    @classmethod
    def increase_total_instances(cls) -> NoReturn:
        cls.total_instances += 1

    @classmethod
    def increase_total_active_heap_node(cls) -> NoReturn:
        cls.total_active_heap_node += 1

    @classmethod
    def decrease_total_active_heap_node(cls) -> NoReturn:
        cls.total_active_heap_node -= 1

    def __init__(self, value: Any = None, prev: Optional['HeapNode'] = None, left: Optional['HeapNode'] = None, right: Optional['HeapNode'] = None):
        self.value = value
        self.prev = prev
        self.left = left
        self.right = right
        HeapNode.increase_total_active_heap_node()
        HeapNode.increase_total_instances()

    def get_value(self) -> Any:
        return self.value

    def put_value(self, value: Any) -> NoReturn:
        self.value = value

    def get_prev(self) -> Optional['HeapNode']:
        return self.prev

    def put_prev(self, prev: Optional['HeapNode']) -> NoReturn:
        self.prev = prev

    def get_left(self) -> Optional['HeapNode']:
        return self.left

    def put_left(self, left: Optional['HeapNode']) -> NoReturn:
        self.left = left

    def get_right(self) -> Optional['HeapNode']:
        return self.right

    def put_right(self, right: Optional['HeapNode']) -> NoReturn:
        self.right = right

    def del_prev(self) -> NoReturn:
        self.prev = None

    def del_value(self) -> NoReturn:
        self.value = None

    def del_left(self) -> NoReturn:
        self.left = None

    def del_right(self) -> NoReturn:
        self.right = None

    def del_left_and_right(self) -> NoReturn:
        self.del_right()
        self.del_left()

    def del_pointers(self) -> NoReturn:
        self.del_left_and_right()
        self.del_prev()

    def clean_node(self) -> NoReturn:
        self.del_pointers()
        self.del_value()

    def __del__(self) -> NoReturn:
        self.clean_node()
        HeapNode.decrease_total_active_heap_node()

    def __repr__(self) -> str:
        return f"HeapNode({self.get_value()!r}, {self.get_prev()!r}, {self.get_left()!r}, {self.get_right()!r})"
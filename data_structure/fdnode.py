from typing import Any, NoReturn, Optional
from copy import deepcopy

class FDNode:
    total_instances = 0
    total_active_nodes = 0

    @classmethod
    def increase_instaces(cls) -> NoReturn:
        cls.total_instances += 1

    @classmethod
    def increase_total_active_nodes(cls) -> NoReturn:
        cls.total_active_nodes += 1

    @classmethod
    def decrease_total_active_nodes(cls) -> NoReturn:
        cls.total_active_nodes -= 1

    @classmethod
    def get_total_instances(cls) -> int:
        return cls.total_instances

    @classmethod
    def get_total_active_nodes(cls) -> int:
        return cls.total_active_nodes
    def __init__(self, value: Any = None, right: Optional['FDNode'] = None, down: Optional['FDNode'] = None, left: Optional['FDNode'] = None, up: Optional['FDNode'] = None) -> NoReturn:
        self.value = value
        self.up = up
        self.right = right
        self.down = down
        self.left = left
        FDNode.increase_total_active_nodes()
        FDNode.increase_instaces()

    def get_value(self) -> Any:
        return self.value

    def put_value(self, value: Any) -> NoReturn:
        self.value = value

    def get_right(self) -> Optional['FDNode']:
        return self.right

    def put_right(self, right: Optional['FDNode']) -> NoReturn:
        self.right = right

    def get_down(self) -> Optional['FDNode']:
        return self.down

    def put_down(self, down: Optional['FDNode']) -> NoReturn:
        self.down = down

    def get_left(self) -> Optional['FDNode']:
        return self.left

    def put_left(self, left: Optional['FDNode']) -> NoReturn:
        self.left = left

    def get_up(self) -> Optional['FDNode']:
        return self.up

    def put_up(self, up: Optional['FDNode']) -> NoReturn:
        self.up = up

    def del_up(self) -> NoReturn:
        self.up = None

    def del_down(self) -> NoReturn:
        self.down = None

    def del_right(self) -> NoReturn:
        self.right = None

    def del_left(self) -> NoReturn:
        self.left = None

    def del_value(self) -> NoReturn:
        self.value = None

    def del_pointers(self) -> NoReturn:
        self.del_up()
        self.del_down()
        self.del_left()
        self.del_right()

    def clean_node(self) -> NoReturn:
        self.del_pointers()
        self.del_value()

    def get_copy(self, deepcp: bool = True) -> Optional['FDNode']:
        if deepcp:
            return deepcopy(self)
        return self

    def __del__(self) -> NoReturn:
        self.clean_node()
        FDNode.decrease_total_active_nodes()

    def __repr__(self) -> str:
        return f"FDNode({self.get_value()!r}, {self.get_right()!r}, {self.get_down()!r}, {self.get_left()!r}, {self.get_up()!r})"
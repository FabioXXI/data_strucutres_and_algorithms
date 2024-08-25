from typing import Optional, NoReturn, Any
from copy import deepcopy

class MultidimensionalNode:
    total_instances = 0
    total_active_nodes = 0

    @classmethod
    def increase_active_nodes(cls) -> NoReturn:
        cls.total_active_nodes += 1

    @classmethod
    def increase_instances(cls) -> NoReturn:
        cls.total_instances += 1

    @classmethod
    def decrease_active_nodes(cls) -> NoReturn:
        cls.total_instances -= 1

    @classmethod
    def get_total_instances(cls) -> int:
        return cls.total_instances

    @classmethod
    def get_total_active_nodes(cls) -> int:
        return cls.total_active_nodes

    def __init__(self, value: Any = None, point_to: Optional['MultidimensionalNode'] | list[Optional['MultidimensionalNode']] = None, pointed_from: Optional['MultidimensionalNode'] | list[Optional['MultidimensionalNode']] = None) -> NoReturn:
        self.value = value
        self.point_to = point_to
        self.pointed_from = pointed_from
        MultidimensionalNode.increase_active_nodes()
        MultidimensionalNode.increase_instances()

    def put_value(self, value: Any) -> NoReturn:
        self.value = value

    def put_point_to(self, point_to: Optional['MultidimensionalNode']) -> NoReturn:
        self.point_to = point_to

    def put_pointed_from(self, pointed_from: Optional['MultidimensionalNode']) -> NoReturn:
        self.pointed_from = pointed_from

    def get_value(self) -> Any:
        return self.value

    def get_point_to(self) -> Optional['MultidimensionalNode'] | list[Optional['MultidimensionalNode']]:
        return self.point_to

    def get_pointed_from(self) -> Optional['MultidimensionalNode'] | list[Optional['MultidimensionalNode']]:
        return self.pointed_from

    def append_point_to(self, node: Optional['MultidimensionalNode']) -> NoReturn:
        if self.point_to:
            if not(type(self.point_to) is list):
                self.point_to = [self.point_to]
            self.point_to.append(node)
            return
        self.point_to = [node]

    def append_pointed_from(self, node: Optional['MultidimensionalNode']) -> NoReturn:
        if self.pointed_from:
            if not(type(self.pointed_from) is list):
                self.pointed_from = [self.pointed_from]
            self.pointed_from.append(node)
            return
        self.pointed_from = [node]

    def pop_point_to(self, index: int = -1) -> Any:
        if self.get_point_to() is None:
            raise "Not point available to be popped"
        if type(self.get_point_to()) is list:
            return self.get_point_to().pop(index)
        raise f"{self.point_to!r} is not a {list!r}"

    def pop_pointed_from(self, index: int = -1) -> Any:
        if self.get_pointed_from() is None:
            raise "Not point available to be popped"
        if type(self.get_pointed_from()) is list:
            return self.get_pointed_from().pop(index)
        raise f"{self.pointed_from!r} is not a {list!r}"

    def remove_point_to(self, value: Any) -> Any:
        if self.get_point_to() is None:
            raise "Not point available to be removed"
        if type(self.get_point_to()) is list:
            for node in self.get_point_to():
                if node == value:
                    index = self.get_point_to().index(node)
                    return self.get_point_to().pop(index)
                return None
        raise f"{self.point_to!r} is not a {list!r}"

    def remove_pointed_from(self, value: Any) -> Any:
        if self.get_pointed_from() is None:
            raise "Not point available to be removed"
        if type(self.get_pointed_from()) is list:
            for node in self.get_pointed_from():
                if node == value:
                    index = self.get_pointed_from().index(node)
                    return self.get_pointed_from().pop(index)
                return None
        raise f"{self.pointed_from!r} is not a {list!r}"

    def del_point_to(self) -> NoReturn:
        self.point_to = None

    def del_pointed_from(self) -> NoReturn:
        self.pointed_from = None

    def del_point_to_and_pointed_from(self) -> NoReturn:
        self.del_point_to()
        self.del_pointed_from()

    def del_value(self) -> NoReturn:
        self.value = None

    def get_copy(self, deepcp: bool = True) -> Optional['MultidimensionalNode']:
        if deepcp:
            return deepcopy(self)
        return self

    def __repr__(self) -> str:
        return f"MultidimensionalNode({self.get_value()!r}, {self.get_point_to()!r}, {self.get_pointed_from()!r})"

    def __del__(self) -> NoReturn:
        self.del_point_to_and_pointed_from()
        MultidimensionalNode.decrease_active_nodes()

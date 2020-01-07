import abc
from typing import List, Callable


class ImplicitLimit(abc.ABC):
    def __init__(self, func: Callable):
        self.func = func

    @abc.abstractmethod
    def check_is_point_within_limit(self, point: List) -> bool:
        pass

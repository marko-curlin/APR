import abc
from typing import List


class ExplicitLimit(abc.ABC):
    def __init__(self, limit_value: List):
        self.limit_value = limit_value

    @abc.abstractmethod
    def is_point_within_limit(self, point: List) -> bool:
        pass
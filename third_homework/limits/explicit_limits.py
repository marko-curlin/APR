import abc
from typing import List


class ExplicitLimit(abc.ABC):
    def __init__(self, limit_value: List[float]):
        self.limit_values = limit_value

    @abc.abstractmethod
    def is_point_within_limit(self, point: List[float]) -> bool:
        pass


class LowerLimit(ExplicitLimit):

    def is_point_within_limit(self, point: List[float]) -> bool:
        for limit_i, coordinate_i in zip(self.limit_values, point):
            if coordinate_i < limit_i:
                return False

        return True


class UpperLimit(ExplicitLimit):

    def is_point_within_limit(self, point: List[float]) -> bool:
        for limit_i, coordinate_i in zip(self.limit_values, point):
            if coordinate_i > limit_i:
                return False

        return True

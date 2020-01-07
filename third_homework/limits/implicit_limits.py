import abc
from typing import List, Callable


class ImplicitLimit(abc.ABC):
    def __init__(self, func: Callable):
        self.func = func

    @abc.abstractmethod
    def is_point_within_limit(self, point: List) -> bool:
        pass


EPSILON = 10e-6


class EquationLimit(ImplicitLimit):

    def is_point_within_limit(self, point: List) -> bool:
        return abs(self.func(*point)) < EPSILON


class InequationLimit(ImplicitLimit):

    def is_point_within_limit(self, point: List) -> bool:
        return self.func(*point) >= 0

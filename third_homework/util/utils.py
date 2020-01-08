from typing import List
from math import sqrt

from third_homework.limits.explicit_limits import ExplicitLimit
from third_homework.limits.implicit_limits import ImplicitLimit

MAX_ITERATIONS = 300


def norm(vector: List[float]) -> float:
    return sqrt(sum([x**2 for x in vector]))


def multiply_each_element(vector: List[float], x: float) -> List[float]:
    return [x * element for element in vector]


def add_elements_on_same_index(vector1: List[float], vector2: List[float]) -> List[float]:
    return [el1 + el2 for el1, el2 in zip(vector1, vector2)]


def sub_elements_on_same_index(vector1: List[float], vector2: List[float]) -> List[float]:
    return [el1 - el2 for el1, el2 in zip(vector1, vector2)]


def mul_elements_on_same_index(vector1: List[float], vector2: List[float]) -> List[float]:
    return [el1 * el2 for el1, el2 in zip(vector1, vector2)]


def is_point_within_limits(point: List[float], *, implicit_limits: List[ImplicitLimit] = (),
                           explicit_limits: List[ExplicitLimit] = ()) -> bool:
    for implicit_limit in implicit_limits:
        if not implicit_limit.is_point_within_limit(point):
            return False

    for explicit_limit in explicit_limits:
        if not explicit_limit.is_point_within_limit(point):
            return False

    return True


def max_diff_on_same_indices(vector1: List[float], vector2: List[float]) -> float:
    return max(map(abs, sub_elements_on_same_index(vector1, vector2)))

from typing import List
from math import sqrt
from copy import deepcopy

from second_homework.golden_section import find_function_min as golden_section_min
from second_homework.function import LambdaFunction


def find_function_min(function, start_point: List[float], e: float = 10**-6) -> List[float]:
    x = start_point
    while True:
        xs = deepcopy(x)

        for i in range(len(x)):
            lambda_function = LambdaFunction(function, x, i)
            x[i] += golden_section_min(lambda_function, start_point=deepcopy(x[i]))

        if norm([_x - _xs for _x, _xs in zip(x, xs)]) < e:
            return x


def norm(vector: List) -> float:
    return sqrt(sum([x**2 for x in vector]))

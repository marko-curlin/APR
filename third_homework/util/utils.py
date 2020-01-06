from typing import List
from math import sqrt


def norm(vector: List) -> float:
    return sqrt(sum([x**2 for x in vector]))


def multiply_each_element(vector: List, x: float) -> List:
    return [x * element for element in vector]


def add_elements_on_same_index(vector1: List, vector2: List) -> List:
    return [el1 + el2 for el1, el2 in zip(vector1, vector2)]


def sub_elements_on_same_index(vector1: List, vector2: List) -> List:
    return [el1 - el2 for el1, el2 in zip(vector1, vector2)]

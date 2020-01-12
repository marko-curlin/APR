from typing import List


def add_elements_on_same_index(vector1: List[float], vector2: List[float]) -> List[float]:
    return [el1 + el2 for el1, el2 in zip(vector1, vector2)]


def set_within_limits(vector, lower_limit, upper_limit):
    new_vector = []

    for el in vector:
        if el < lower_limit:
            new_vector.append(lower_limit)
        elif el > upper_limit:
            new_vector.append(upper_limit)
        else:
            new_vector.append(el)

    return new_vector


def square_list_elements(vector):
    return [el ** 2 for el in vector]

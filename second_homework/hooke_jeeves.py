from typing import List
from copy import deepcopy
from operator import add, sub


def find_function_min(function, start_point: List[float], delta_x: float,
                      epsilon: float = 10**-6, enable_output = False) -> List[float]:
    Xp = deepcopy(start_point)
    Xb = deepcopy(start_point)

    while True:
        Xn = explore(function, Xp, delta_x)

        if enable_output:
            print_values(function, Xb, Xp, Xn)

        if function(*Xn) < function(*Xb):
            Xp = subtract_list_elements(multiply_list_elements(Xn, 2), Xb)
            Xb = Xn

        else:
            delta_x /= 2
            Xp = Xb

        if delta_x < epsilon:
            break

    return Xb


def explore(function, explore_point, delta_x):
    new_point = deepcopy(explore_point)

    for i in range(len(new_point)):
        current_value = function(*new_point)

        new_point[i] += delta_x
        new_value = function(*new_point)

        if new_value > current_value:
            new_point[i] -= 2 * delta_x
            new_value = function(*new_point)

            if new_value > current_value:
                new_point[i] += delta_x

    return new_point


def subtract_list_elements(list1, list2):
    return list(map(sub, list1, list2))


def add_list_elements(list1, list2):
    return list(map(add, list1, list2))


def multiply_list_elements(_list, mul):
    return [mul * x for x in _list]


def print_values(function, base_point, explore_point, new_point):
    value_Xb = function(*base_point)
    value_Xp = function(*explore_point)
    value_Xn = function(*new_point)

    print("Xb = {}, f(Xb) = {} ... Xp = {}, f(Xp) = {} ... Xn = {}, f(Xn) = {}".format(base_point, value_Xb,
                                                                                       explore_point, value_Xp,
                                                                                       new_point, value_Xn))


if __name__ == '__main__':
    print(find_function_min(lambda x, y: x**2 + 4 * y**2, [7, 3], 1, 0.1, enable_output=True))

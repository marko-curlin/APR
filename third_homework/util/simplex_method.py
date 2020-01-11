from typing import List, Tuple, Callable
from operator import sub
from copy import deepcopy
from math import sqrt
from prettytable import PrettyTable

from third_homework.functions.function import InnerPointFunction
from third_homework.util.utils import add_elements_on_same_index, multiply_each_element


def find_function_min(function: Callable, start_point: List[float], start_delta: float = 1, alpha: float = 1, beta: float = 0.5,
                      gama: float = 2, sigma: float = 0.5, epsilon: float = 10**-6, enable_output=False) -> List[float]:
    simplex_points = calculate_simplex_points(start_point, start_delta)

    table = PrettyTable(['x' + str(i) for i in range(len(start_point))] + ['value of function in centroid'])

    while True:
        h, l = get_lowest_and_highest_point(function, simplex_points)

        Xc: List[float] = calculate_centroid(simplex_points, h)

        if enable_output:
            table.add_row([centroid_value for centroid_value in Xc] + [function(*Xc)])

        Xr: List[float] = reflection(Xc, simplex_points[h], alpha)

        if function(*Xr) < function(*simplex_points[l]):
            Xe = expansion(Xc, Xr, gama)

            if function(*Xe) < function(*simplex_points[l]):
                simplex_points[h] = Xe
            else:
                simplex_points[h] = Xr

        else:
            if check_fXr_larger_than_all_except_fXh(function, Xr, simplex_points, h):
                if function(*Xr) < function(*simplex_points[h]):
                    simplex_points[h] = Xr

                Xk = contraction(Xc, simplex_points[h], beta)

                if function(*Xk) < function(*simplex_points[h]):
                    simplex_points[h] = Xk
                else:
                    move_all_points_to_Xl(simplex_points, l, sigma)

            else:
                simplex_points[h] = Xr

        if check_stop_condition(function, simplex_points, Xc, epsilon):
            break

    if enable_output:
        print(table)

    return Xc


def calculate_simplex_points(start_point, start_delta):
    simplex_points = []

    for i in range(len(start_point) + 1):
        simplex_points.append(deepcopy(start_point))

    for i in range(len(start_point)):
        simplex_points[i][i] += start_delta

    return simplex_points


def get_lowest_and_highest_point(function, simplex_points: List[List[float]]) -> Tuple[int, int]:
    function_values_in_points = [(i, function(*simplex_point)) for i, simplex_point in enumerate(simplex_points)]

    highest = max(function_values_in_points, key=lambda x: x[1])[0]

    lowest = min(function_values_in_points, key=lambda x: x[1])[0]

    return highest, lowest


def calculate_centroid(simplex_points, h):
    centroid = [0] * len(simplex_points[0])

    for i in range(len(simplex_points)):
        if i == h:
            continue

        centroid = add_elements_on_same_index(centroid, simplex_points[i])

    centroid = multiply_each_element(centroid, 1 / (len(simplex_points) - 1))

    return centroid


def reflection(centroid: List[float], worst_point: List[float], alpha: float):
    # reflected_point = []
    #
    # for i in range(len(centroid)):
    #     i_th_coordinate_of_reflected_point = (1 + alpha) * centroid[i] - alpha * worst_point[i]
    #     reflected_point.append(i_th_coordinate_of_reflected_point)
    #
    # return reflected_point
    return [(1 + alpha) * c_i - alpha * wp_i for c_i, wp_i in zip(centroid, worst_point)]


def expansion(centroid, reflected_point, gama):
    return reflection(centroid, reflected_point, -gama)


def check_fXr_larger_than_all_except_fXh(function, reflected_point, simplex_points, h):
    value_in_reflected_point = function(*reflected_point)

    for i in range(len(simplex_points)):
        if i == h:
            continue

        if value_in_reflected_point <= function(*simplex_points[i]):
            return False

    return True


def contraction(centroid, worst_point, beta):
    return expansion(centroid, worst_point, beta)


def move_all_points_to_Xl(simplex_points, l, sigma):
    for i in range(len(simplex_points)):
        if i == l:
            continue

        simplex_points[i] = add_elements_on_same_index(simplex_points[i], simplex_points[l])
        simplex_points[i] = [x_i * sigma for x_i in simplex_points[i]]


def check_stop_condition(function, simplex_points, centroid, epsilon):
    if isinstance(function, InnerPointFunction) and function(*centroid) == 0:
        return True

    _sum = 0

    value_in_centroid = function(*centroid)

    for simplex_point in simplex_points:
        _sum += (function(*simplex_point) - value_in_centroid)**2

    return sqrt(_sum / len(simplex_points[0])) <= epsilon


def subtract_list_elements(list1, list2):
    return list(map(sub, list1, list2))


if __name__ == '__main__':
    print(find_function_min(lambda x, y: x**2 + y**2, [2, 0], enable_output=True))

    print(find_function_min(lambda x, y: 100 * (y - x) ** 2 + (1 - x) ** 2, [-1.9, 2], enable_output=True))

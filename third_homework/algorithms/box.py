from math import inf
from random import random

from third_homework.functions.function import Function
from third_homework.util.utils import *
from third_homework.limits.implicit_limits import ImplicitLimit
from third_homework.limits.explicit_limits import ExplicitLimit, LowerLimit, UpperLimit


def find_function_min(function: Function, start_point: List[float], implicit_limits: List[ImplicitLimit] = None,
                      explicit_limits: List[ExplicitLimit] = None, e: float = 10**-6, alpha: float = 1.3,
                      enable_output=False) -> List[float]:
    if not is_point_within_limits(start_point, implicit_limits=implicit_limits, explicit_limits=explicit_limits):
        raise ValueError('Starting point is not within limits!')

    simplex_points: List[List[float]] = [start_point]
    Xc = start_point
    lower_limit = get_max_lower_limit(explicit_limits)
    upper_limit = get_min_upper_limit(explicit_limits)
    for t in range(2*len(start_point)):
        Xt = get_random_point(explicit_limits)

        while not is_point_within_limits(Xt, implicit_limits=implicit_limits):
            Xt = move_first_point_towards_second(Xt, Xc)

        simplex_points.append(Xt)
        Xc = calculate_centroid(simplex_points, None)

    while True:
        h, h2 = find_worst_and_second_worst_index(simplex_points, function)

        Xc = calculate_centroid(simplex_points, h)

        Xr = reflection(Xc, simplex_points[h], alpha)

        Xr = move_point_to_within_limits(lower_limit, upper_limit, Xr)

        while not is_point_within_limits(Xr, implicit_limits=implicit_limits):
            Xr = move_first_point_towards_second(Xr, Xc)

        if function(*Xr) > function(*simplex_points[h2]):
            Xr = move_first_point_towards_second(Xr, Xc)

        simplex_points[h] = Xr

        if is_stop_condition_satisfied(function, simplex_points, Xc, e):
            break

    return Xc


def get_max_lower_limit(explicit_limits: List[ExplicitLimit]) -> List[float]:
    all_limit_values = list(map(lambda x: x.limit_values, filter(lambda x: isinstance(x, LowerLimit), explicit_limits)))
    max_lower_limits = []
    for limits_i in zip(*all_limit_values):
        max_lower_limits.append(max(limits_i))
    return max_lower_limits


def get_min_upper_limit(explicit_limits: List[ExplicitLimit]) -> List[float]:
    all_limit_values = list(map(lambda x: x.limit_values, filter(lambda x: isinstance(x, UpperLimit), explicit_limits)))
    min_upper_limits = []
    for limits_i in zip(*all_limit_values):
        min_upper_limits.append(min(limits_i))
    return min_upper_limits


def get_random_point(explicit_limits):
    lower_limit = get_max_lower_limit(explicit_limits)
    upper_limit = get_min_upper_limit(explicit_limits)

    random_point = sub_elements_on_same_index(upper_limit, lower_limit)
    random_point = multiply_each_element(random_point, random())
    random_point = add_elements_on_same_index(lower_limit, random_point)
    return random_point


def is_point_within_limits(point: List[float], *, implicit_limits: List[ImplicitLimit] = None,
                           explicit_limits: List[ExplicitLimit] = None) -> bool:
    for implicit_limit in implicit_limits:
        if not implicit_limit.is_point_within_limit(point):
            return False

    for explicit_limit in explicit_limits:
        if not explicit_limit.is_point_within_limit(point):
            return False

    return True


def move_first_point_towards_second(Xt, Xc):
    closer_point = add_elements_on_same_index(Xt, Xc)
    closer_point = multiply_each_element(closer_point, 0.5)
    return closer_point


def find_worst_and_second_worst_index(simplex_points: List[List[float]], func: Function):
    simplex_values = [func(*point) for point in simplex_points]
    if len(simplex_values) <= 1:
        return 0, None
    elif len(simplex_values) <= 2:
        return simplex_values.index(max(simplex_values)), simplex_values.index(min(simplex_values))

    max_value = -inf
    max_index = -1
    second_max_value = -inf
    second_max_index = -1

    for index, value in enumerate(simplex_values):
        if value > second_max_value:
            if value > max_value:
                max_index, second_max_index = index, max_index
            else:
                second_max_index = index

    return max_index, second_max_index


def move_point_to_within_limits(lower_limit: List[float], upper_limit: List[float], point: List[float]) -> List[float]:
    moved_point = []
    for lower_limit_coordinate, upper_limit_coordinate, point_coordinate in zip(lower_limit, upper_limit, point):
        if point_coordinate < lower_limit_coordinate:
            new_coordinate = lower_limit_coordinate
        elif point_coordinate > upper_limit_coordinate:
            new_coordinate = upper_limit_coordinate
        else:
            new_coordinate = point_coordinate

        moved_point.append(new_coordinate)

    return moved_point


def calculate_centroid(simplex_points: List[List[float]], h: int) -> List[float]:
    centroid = [0] * len(simplex_points[0])

    for i in range(len(simplex_points)):
        if i == h:
            continue

        centroid = add_elements_on_same_index(centroid, simplex_points[i])

    centroid = multiply_each_element(centroid, 1 / (len(simplex_points) - 1))  # [centroid_coordinate / (len(simplex_points) - 1) for centroid_coordinate in centroid]

    return centroid


def reflection(centroid: List[float], worst_point: List[float], alpha: float):
    return [(1 + alpha) * c_i - alpha * wp_i for c_i, wp_i in zip(centroid, worst_point)]


def is_stop_condition_satisfied(function, simplex_points, centroid, epsilon):
    _sum = 0

    value_in_centroid = function(*centroid)

    for simplex_point in simplex_points:
        _sum += (function(*simplex_point) - value_in_centroid)**2

    return sqrt(_sum / len(simplex_points[0])) <= epsilon

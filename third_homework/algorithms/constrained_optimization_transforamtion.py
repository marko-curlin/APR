from copy import deepcopy

from prettytable import PrettyTable

from third_homework.functions.function import Function, InnerPointFunction, TransformedFunction
from third_homework.util.utils import *
from third_homework.util.simplex_method import find_function_min as simplex_min


def find_function_min(function: Function, start_point: List[float], implicit_limits: List[ImplicitLimit] = None,
                      t: float = 1, e: float = 10**-6, enable_output=False) -> List[float]:
    table = PrettyTable(['total_iterations', 'previous_point', 'current_point', 'min_value', 'break_condition_value'])
    start_point = list(start_point)

    if is_point_within_limits(start_point, implicit_limits=implicit_limits):
        current_point = start_point
    else:
        current_point = find_inner_point(start_point, implicit_limits)

    function = TransformedFunction(function, implicit_limits, t)
    minimum_value = function(*current_point)

    total_iterations, iterations_without_improvement = 1, 0
    while True:
        previous_point = deepcopy(current_point)

        current_point = simplex_min(function, current_point)

        if max_diff_on_same_indices(previous_point, current_point) < e:
            break

        current_value = function(*current_point)

        table.add_row([total_iterations+1, previous_point, current_point, minimum_value, max_diff_on_same_indices(previous_point, current_point)])

        if current_value < minimum_value:
            minimum_value = current_value
            iterations_without_improvement = 0
        else:
            iterations_without_improvement += 1
            if iterations_without_improvement == MAX_ITERATIONS:
                if enable_output:
                    print(table)
                raise ArithmeticError('It exceeded maximum nr of iterations')

        total_iterations += 1

        function.t *= 10

    if enable_output:
        print(table)

    return current_point


def find_inner_point(start_point, implicit_limits):
    inner_point_function = InnerPointFunction(implicit_limits)
    return simplex_min(inner_point_function, start_point)

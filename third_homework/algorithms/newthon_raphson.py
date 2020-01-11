from third_homework.functions.function import Function, LambdaFunction
from copy import deepcopy
from third_homework.util.utils import *
from third_homework.functions.function_factory import get_function_and_start_point
from third_homework.util.matrix_utils import solve_equation, matrix_inverse
from third_homework.util.matrix import Matrix
from third_homework.util import golden_section

from prettytable import PrettyTable


def find_function_min(function: Function, start_point: List[float], shift_type='classic', e: float = 10**-6,
                      enable_output=False) -> List[float]:
    output = PrettyTable(['total_iterations', 'current_point', 'gradient', 'shift'])

    total_iterations = 0
    iterations_without_improvement = 0

    minimum_value = function(*start_point)
    current_point = deepcopy(start_point)

    while True:
        gradient = function.calculate_gradient(*current_point)
        hesse_matrix = function.calculate_hesse_matrix(*current_point)

        current_shift = solve_equation(Matrix(hesse_matrix), Matrix([[el] for el in gradient])).as_list()[0]

        if norm(current_shift) < e:
            break

        if shift_type == 'classic':
            shift = calculate_shift_for_classic(current_shift)
        elif shift_type == 'golden':
            shift = calculate_shift_for_golden(function, current_point, current_shift)
        else:
            raise ValueError('unsupported shift type')

        output.add_row([total_iterations + 1, current_point, current_shift, shift])

        current_point = add_elements_on_same_index(current_point, shift)

        current_value = function(*current_point)
        if current_value < minimum_value:
            minimum_value = current_value
            iterations_without_improvement = 0
        else:
            iterations_without_improvement += 1
            if iterations_without_improvement == MAX_ITERATIONS:
                if enable_output:
                    print(output)
                raise ArithmeticError('It exceeded maximum nr of iterations')

        total_iterations += 1

    if enable_output:
        print(output)

    return current_point


def calculate_shift_for_classic(gradient):
    shift = deepcopy(gradient)
    shift = multiply_each_element(shift, -1)
    return shift


def calculate_shift_for_golden(function, current_point, shift):
    lambda_function = LambdaFunction(function, current_point, shift)
    return multiply_each_element(shift, golden_section.find_function_min(lambda_function, start_point=0))


if __name__ == '__main__':
    print(find_function_min(*get_function_and_start_point(1), shift_type='golden', enable_output=True))

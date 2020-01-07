from prettytable import PrettyTable

from third_homework.algorithms.gradient import find_function_min as gradient
from third_homework.algorithms.newthon_raphson import find_function_min as newton_raphson
from third_homework.algorithms.box import find_function_min as box

from third_homework.functions.function_factory import get_function_and_start_point

from third_homework.limits.implicit_limits import InequationLimit
from third_homework.limits.explicit_limits import LowerLimit, UpperLimit

PRINT_STEPS = False


def main():
    # print_headers('FIRST TASK', '#'*70)
    # first_task()
    # first_task_golden()
    # print_headers('SECOND TASK', '#' * 70)
    # second_task()
    print_headers('THIRD TASK', '#' * 70)
    third_task()


def print_headers(title, marker):
    print("{} {} {}".format(marker, title, marker))


def first_task():
    print_headers('Using whole gradient step', '-'*10)
    try:
        gradient(*get_function_and_start_point(3), enable_output=PRINT_STEPS)
    except ArithmeticError as e:
        print(e)


def first_task_golden():
    print_headers('Using golden step', '-'*10)
    func, start_point = get_function_and_start_point(3)
    result = gradient(func, start_point, shift_type='golden', enable_output=PRINT_STEPS)
    print_result(result, func)


def second_task():
    print_headers('GRADIENT', '$'*20)

    print_headers('First function', '-'*10)
    func, start_point = get_function_and_start_point(1)
    result = gradient(func, start_point, shift_type='golden', enable_output=PRINT_STEPS)
    print_result(result, func)

    print_headers('Second function', '-'*10)
    func, start_point = get_function_and_start_point(2)
    result = gradient(func, start_point, shift_type='golden', enable_output=PRINT_STEPS)
    print_result(result, func)

    print_headers('NEWTON-RAPHSON', '$'*20)

    print_headers('First function', '-'*10)
    func, start_point = get_function_and_start_point(1)
    result = newton_raphson(func, start_point, shift_type='golden', enable_output=PRINT_STEPS)
    print_result(result, func)

    print_headers('Second function', '-'*10)
    func, start_point = get_function_and_start_point(2)
    result = newton_raphson(func, start_point, shift_type='golden', enable_output=PRINT_STEPS)
    print_result(result, func)


def third_task():
    implicit_limit1 = InequationLimit(lambda x, y: y - x)
    implicit_limit2 = InequationLimit(lambda x, y: 2 - x)
    explicit_limit1 = LowerLimit([-100, -100])
    explicit_limit2 = UpperLimit([100, 100])

    print_headers('BOX', '$' * 20)

    print_headers('First function', '-' * 10)
    func, start_point = get_function_and_start_point(1)
    result = box(func, start_point, [implicit_limit1, implicit_limit2], [explicit_limit1, explicit_limit2])
    print_result(result, func)

    print_headers('Second function', '-' * 10)
    func, start_point = get_function_and_start_point(2)
    result = box(func, start_point, [implicit_limit1, implicit_limit2], [explicit_limit1, explicit_limit2])
    print_result(result, func)


def print_result(result, function):
    table = PrettyTable(['min', 'function value in min', 'function calls', 'total function calls', 'gradient calls',
                         'Hesse matrix calls'])
    result_value = function(*result if isinstance(result, list) else [result])
    table.add_row([result, result_value if not isinstance(result_value, list) else tuple(result_value),
                   function.nr_of_calls, function.total_nr_of_calls, function.gradient_calls, function.Hesse_matrix_calls])
    print(table)


if __name__ == '__main__':
    main()

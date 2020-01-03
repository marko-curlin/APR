from prettytable import PrettyTable

from third_homework.gradient import find_function_min as gradient
from third_homework.functions.function_factory import get_function_and_start_point

PRINT_STEPS = False


def main():
    print_headers('FIRST TASK', '#'*70)
    first_task()
    first_task_golden()


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


def print_result(result, function):
    table = PrettyTable(['min', 'function value in min', 'function calls', 'total function calls', 'gradient calls',
                         'Hesse matrix calls'])
    result_value = function(*result if isinstance(result, list) else [result])
    table.add_row([result, result_value if not isinstance(result_value, list) else tuple(result_value),
                   function.nr_of_calls, function.total_nr_of_calls, function.gradient_calls, function.Hesse_matrix_calls])
    print(table)


if __name__ == '__main__':
    main()

from math import sqrt, sin
from operator import mul
from copy import deepcopy
from random import random
from prettytable import PrettyTable

from second_homework.function import Function
from second_homework.golden_section import find_function_min as golden_section
from second_homework.search_on_coordinate_axis import find_function_min as coordinate_axis
from second_homework.simplex_method import find_function_min as simplex
from second_homework.hooke_jeeves import find_function_min as hooke_jeeves


def function_factory(func_nr: int):
    if func_nr not in range(1, 7):
        raise ValueError('Available functions are in range: [1, 6]')

    if func_nr == 1:
        return Function(lambda x, y: 100 * (y - x) ** 2 + (1 - x) ** 2), [-1.9, 2]
    if func_nr == 2:
        return Function(lambda x, y: (x - 4)**2 + 4 * (y - 2)**2), [4, 2]
    if func_nr == 3:
        return Function(lambda *x: sum([(x[i] - i)**2 for i in range(len(x))])), [0, 0, 0, 0, 0]
    if func_nr == 4:
        return Function(lambda x, y: abs((x - y) * (x + y)) + sqrt(x**2 + y**2)), [5.1, 1.1]
    if func_nr == 6:
        return Function(lambda *x: 0.5 + (sin(sqrt(sum(square_list_elements(x))))**2 - 0.5)
                                       / (1 + 0.001 * sum(square_list_elements(x)))**2), [0]


def square_list_elements(list1):
    return list(map(mul, list1, list1))


def print_headers(title, marker):
    print("{} {} {}".format(marker, title, marker))


def main():
    print_headers('FIRST TASK (10)', '$'*100)
    task1(10)
    print_headers('FIRST TASK (50)', '$'*100)
    task1(50)
    print_headers('FIRST TASK (100)', '$'*100)
    task1(100)
    print_headers('FIRST TASK (1000)', '$'*100)
    task1(1000)
    print_headers('SECOND TASK', '$'*100)
    task2()
    print_headers('THIRD TASK', '$'*100)
    task3()
    print_headers('FOURTH TASK', '$'*100)
    task4()
    print_headers('FIFTH TASK', '$'*100)
    task5()


def all_algorithms(original_function, start_point):
    print_headers('GOLDEN SECTION', '#'*70)
    func = deepcopy(original_function)
    result = golden_section(func, start_point=start_point, enable_output=True)
    print_result(func, result)

    print_headers('AXIS SEARCH', '#'*70)
    func = deepcopy(original_function)
    result = coordinate_axis(func, start_point=start_point if isinstance(start_point, list) else [start_point])
    print_result(func, result)

    simplex_and_hooke_jeeves(original_function, start_point)


def simplex_and_hooke_jeeves(original_function, start_point):
    print_headers('SIMPLEX', '#'*70)
    func = deepcopy(original_function)
    result = simplex(func, start_point=start_point if isinstance(start_point, list) else [start_point],
                     enable_output=True)
    print_result(func, result)

    print_headers('HOOKE AND JEEVES', '#'*70)
    func = deepcopy(original_function)
    result = hooke_jeeves(func, start_point=start_point if isinstance(start_point, list) else [start_point],
                          enable_output=True)
    print_result(func, result)


def task1(start_point):
    all_algorithms(Function(lambda x: (x - 3) ** 2), start_point)


def task2():
    for i in range(1, 5):
        original_func, start_point = function_factory(i)
        print('Function number: ' + str(i))
        print('Start point: ' + str(start_point))
        simplex_and_hooke_jeeves(original_func, start_point)

        print_headers('AXIS SEARCH', '#' * 70)
        func = deepcopy(original_func)
        result = coordinate_axis(func, start_point if isinstance(start_point, list) else [start_point])
        print_result(func, result)


def task3():
    func, _ = function_factory(4)
    start_point = [5, 5]

    simplex_and_hooke_jeeves(func, start_point)


def task4():
    original_function, _ = function_factory(1)

    start_point = [0.5, 0.5]
    for i in range(1, 21):
        print_headers('SIMPLEX', '#' * 70)
        print('start point = {}'.format(start_point))
        print('start delta = {}'.format(i))
        func = deepcopy(original_function)
        result = simplex(func, start_point=start_point, start_delta=i, enable_output=True)
        print_result(func, result)

    start_point = [20, 20]
    for i in range(1, 21):
        print_headers('SIMPLEX', '#'*70)
        print('start point = {}'.format(start_point))
        print('start delta = {}'.format(i))
        func = deepcopy(original_function)
        result = simplex(func, start_point=start_point, start_delta=i, enable_output=True)
        print_result(func, result)


def task5():
    original_function, _ = function_factory(6)

    for i in range(5):
        start_point = [random() * 100 - 50, random() * 100 - 50]
        print_headers('SIMPLEX', '#'*70)
        print('start point = {}'.format(start_point))
        func = deepcopy(original_function)
        result = simplex(func, start_point, enable_output=True)
        print_result(func, result)

    start_point = [.001, -0.01]
    print_headers('SIMPLEX', '#' * 70)
    print('start point = {}'.format(start_point))
    func = deepcopy(original_function)
    result = simplex(func, start_point, enable_output=True)
    print_result(func, result)


def print_result(function, result):
    table = PrettyTable(['min', 'function value in min', 'function calls', 'total function calls'])
    result_value = function(*result if isinstance(result, list) else [result])
    table.add_row([result, result_value if not isinstance(result_value, list) else tuple(result_value),
                   function.nr_of_calls, function.total_nr_of_calls])
    print(table)


if __name__ == '__main__':
    main()

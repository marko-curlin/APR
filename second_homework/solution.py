from math import sqrt, sin
from operator import mul
from copy import deepcopy
from random import random

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


def main():
    task1(10)
    task1(50)
    task1(100)
    task2()
    task3()
    task4()
    task5()


def all_algorithms(original_function, start_point):
    func = deepcopy(original_function)
    result = golden_section(func, start_point=start_point, enable_output=True)
    print_result(func, result)

    func = deepcopy(original_function)
    result = coordinate_axis(func, start_point=start_point if isinstance(start_point, list) else [start_point])
    print_result(func, result)

    simplex_and_hooke_jeeves(original_function, start_point)


def simplex_and_hooke_jeeves(original_function, start_point):
    func = deepcopy(original_function)
    result = simplex(func, start_point=start_point if isinstance(start_point, list) else [start_point],
                     enable_output=True)
    print_result(func, result)

    func = deepcopy(original_function)
    result = hooke_jeeves(func, start_point=start_point if isinstance(start_point, list) else [start_point],
                          enable_output=True)
    print_result(func, result)


def task1(start_point):
    all_algorithms(lambda x: (x - 3) ** 2, start_point)


def task2():
    for i in range(1, 4):
        func, start_point = function_factory(i)
        simplex_and_hooke_jeeves(func, start_point)


def task3():
    func, _ = function_factory(4)
    start_point = [5, 5]

    simplex_and_hooke_jeeves(func, start_point)


def task4():
    original_function, _ = function_factory(1)

    start_point = [0.5, 0.5]
    for i in range(1, 21):
        func = deepcopy(original_function)
        result = simplex(func, start_point=start_point, start_delta=i, enable_output=True)
        print_result(func, result)

    start_point = [20, 20]
    for i in range(1, 21):
        func = deepcopy(original_function)
        result = simplex(func, start_point=start_point, start_delta=i, enable_output=True)
        print_result(func, result)


def task5():
    original_function, _ = function_factory(6)

    for i in range(5):
        start_point = [random() * 100 - 50, random() * 100 - 50]
        func = deepcopy(original_function)
        result = simplex(func, start_point, enable_output=True)
        print_result(func, result)

    start_point = [.001, -0.01]
    func = deepcopy(original_function)
    result = simplex(func, start_point, enable_output=True)
    print_result(func, result)


def print_result(function, result):  # TODO: use the function variable; make it prettier
    print(result)


if __name__ == '__main__':
    main()

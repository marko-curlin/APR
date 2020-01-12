from math import sin, sqrt

from fourth_homework.utils import square_list_elements


def function_factory(func_nr: int):
    if func_nr == 1:
        return lambda x, y: 100 * (y - x**2)**2 + (1 - x)**2

    if func_nr == 3:
        return lambda *x: sum([(x[i] - i)**2 for i in range(len(x))])

    if func_nr == 6:
        return lambda *x: 0.5 + (sin(sqrt(sum(square_list_elements(x))))**2 - 0.5) / (1 + 0.001 * sum(square_list_elements(x)))**2

    if func_nr == 7:
        return lambda *x: sum(square_list_elements(x))**0.25 * (1 + sin(50 * sum(square_list_elements(x))**0.1)**2)

    raise ValueError('No function with that index exists.')

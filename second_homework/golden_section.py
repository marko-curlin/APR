from second_homework.unimodal_interval import find_unimodal_interval
from math import sqrt
from typing import Tuple

K = 0.5 * (sqrt(5) - 1)


def find_function_min(function, a: float = None, b: float = None, start_point: float = None, e: float = 10**-6) -> float:
    if a is None or b is None:
        if start_point is None:
            raise ValueError("If either 'a' or 'b' are not provided, the 'start_point' MUST be provided!")

        a, b = find_unimodal_interval(1, start_point, function)

    return sum(find_smallest_interval(function, a, b, e)) / 2


def find_smallest_interval(function, a: float, b: float, e: float) -> Tuple[float, float]:
    c = b - K * (b - a)
    d = a + K * (b - a)

    fc = function(c)
    fd = function(d)

    print_values(function, a, b, c, d)

    while b - a > e:
        if fc < fd:
            b = d
            d = c
            c = b - K * (b - a)

            fd = fc
            fc = function(c)

            print_values(function, a, b, c, d)
        else:
            a = c
            c = d
            d = a + K * (b - a)

            fc = fd
            fd = function(d)

            print_values(function, a, b, c, d)

    return a, b


def print_values(function, a, b, c, d):
    fa = function(a)
    fb = function(b)
    fc = function(c)
    fd = function(d)

    print(('f({: 3f}) = {: 3f}    ' * 4).format(a, fa, b, fb, c, fc, d, fd))


if __name__ == '__main__':
    print(find_function_min(lambda x: (x - 4)**2, a=-2, b=6, start_point=0))

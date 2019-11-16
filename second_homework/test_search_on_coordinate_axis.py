from pytest import approx

from second_homework.search_on_coordinate_axis import find_function_min


def test_search_on_coordinate_axis1():
    assert find_function_min(lambda x, y: 2 * x ** 2 + 2 * x * y + 2 * y ** 2 - 6 * x, [1, 1]) == \
           [approx(2, abs=10**-6), approx(-1, abs=10**-6)]


def test_search_on_coordinate_axis2():
    assert find_function_min(lambda x, y: 100 * (y - x) ** 2 + (1 - x) ** 2, [-1.9, 2]) == \
           [approx(1, abs=10**-4), approx(1, abs=10**-4)]

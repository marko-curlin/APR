from second_homework.unimodal_interval import find_unimodal_interval


def test_unimodal_interval1():
    assert find_unimodal_interval(1, 100, lambda x: x**2 - 2) == (-156, 36)


def test_unimodal_interval2():
    assert find_unimodal_interval(1, 0, lambda x: (x - 4)**2) == (2, 8)

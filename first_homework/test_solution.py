from first_homework.solution import *
import pytest


def test_backward_substitution1():
    matrix = Matrix([[2, 2, 3], [0, 1, -3], [0, 0, 14]])
    vector = Matrix([[25, -15, 75]])

    # assert backward_substitution(matrix, vector).matrix == [pytest.approx([5, 0, 5], abs=0.1)]


def test_backward_substitution2():
    matrix = Matrix([[5, 6, 3], [0, 1.4, 2.2], [0, 0, -1.856]])
    vector = Matrix([[10.3, 6.32, -5.569]])

    assert backward_substitution(matrix, vector).matrix == [pytest.approx([0.5, -0.2, 3], abs=0.1)]


def test_forward_substitution3():
    matrix = Matrix([[1, 0, 0], [1/3, 1, 0], [0, 12/7, 0]])
    vector = Matrix([[2, 3, 4]])

    assert forward_substitution(matrix, vector).matrix == [[2, 7/3, 0]]


def test_LU_decomposition():
    matrix = Matrix([[4,3,2,1], [4,6,1,-1], [-8,3,-5,-6], [12,12,7,4]])

    assert LU_decomposition(matrix).matrix == [[4,3,2,1], [1,3,-1,-2], [-2,3,2,2], [3,1,1,1]]


# def test_LUP_decomposition():
#     matrix = Matrix([[4,3,2,1], [4,6,1,-1], [-8,3,-5,-6], [12,12,7,4]])
#
#     assert LUP_decomposition(matrix).matrix == [[4,3,2,1], [1,3,-1,-2], [-2,3,2,2], [3,1,1,1]]


def test_LUP_decomposition1():
    matrix = Matrix([[3,2,1],[1,2,2],[4,3,4]])

    assert LUP_decomposition(matrix).matrix == [[4, 3, 4], [1/4, 5/4, 1], [3/4, -1/5, -9/5]]

from first_homework.solution import *

from copy import deepcopy
import pytest


def test_assignment_of_whole_row():
    matrix = Matrix([[1.01, 2.1], [3, 4]])
    matrix[0] = [1, 2]

    assert matrix.matrix == [[1, 2], [3, 4]]


def test_transposition():
    matrix = Matrix([[0, 1]])
    matrix.transpose()

    assert matrix.matrix == [[0], [1]]


def test_equality_implementation():
    matrix = Matrix([[0, 1]])

    assert matrix == deepcopy(matrix)


def test_getting_items():
    matrix = Matrix([[1,2], [3,4]])

    assert matrix[0] == [1, 2]

    assert matrix[1][1] == 4

    with pytest.raises(IndexError):
        a = matrix[2]


def test_assignment_of_single_value():
    matrix = Matrix([[1, 2], [3, 4]])

    matrix[0][1] = 5

    assert matrix.matrix[0][1] == 5

    matrix[0][1] += 5

    assert matrix.matrix[0][1] == 10


def test_imul():
    matrix = Matrix([[1, 2], [3, 4]])

    matrix *= 2

    comparison_matrix = [i*2 for i in range(1, 5)]

    for i in range(matrix.rows):
        for j in range(matrix.cols):
            assert matrix.matrix[i][j] == pytest.approx(comparison_matrix[i * matrix.cols + j], 0.1)


def test_square_matrix_function():
    matrix = Matrix([[1,2,3]]*3)

    assert matrix.is_square()

    matrix = Matrix([[1, 2, 3]] * 4)

    assert not matrix.is_square()


def test_column_switch():
    matrix = Matrix([[1,2,3]]*3)

    matrix.switch_columns(1, 2)

    comparison_matrix = [[1,3,2]]*3

    for i in range(matrix.rows):
        for j in range(matrix.cols):
            assert matrix.matrix[i][j] == pytest.approx(comparison_matrix[i][j], 0.1)

from first_homework.solution import *
import pytest

EPSILON = 0.001

@pytest.mark.parametrize(
    'matrix, vector, solution',
    [
        ([[5, 6, 3], [0, 1.4, 2.2], [0, 0, -1.856]], [[10.3, 6.32, -5.569]], [0.5, -0.2, 3])
    ]
)
def test_backward_substitution(matrix, vector, solution):
    matrix = Matrix(matrix)
    vector = Matrix(vector)

    assert backward_substitution(matrix, vector).matrix == [pytest.approx(solution, abs=EPSILON)]

@pytest.mark.parametrize(
    'matrix, vector, solution',
    [
        ([[1, 0, 0], [1 / 3, 1, 0], [0, 12 / 7, 0]], [[2, 3, 4]], [2, 7/3, 0])
    ]
)
def test_forward_substitution(matrix, vector, solution):
    matrix = Matrix(matrix)
    vector = Matrix(vector)

    assert forward_substitution(matrix, vector).matrix == [pytest.approx(solution, abs=EPSILON)]


def test_LU_decomposition():
    matrix = Matrix([[4,3,2,1], [4,6,1,-1], [-8,3,-5,-6], [12,12,7,4]])

    assert LU_decomposition(matrix).matrix == [[4,3,2,1], [1,3,-1,-2], [-2,3,2,2], [3,1,1,1]]


def test_LUP_decomposition2():
    matrix = Matrix([[1,2,0], [3,5,4], [5,6,3]])

    assert LUP_decomposition(matrix)[0].matrix == [pytest.approx([5, 6, 3], abs=EPSILON),
                                                   pytest.approx([0.6, 1.4, 2.2], abs=EPSILON),
                                                   pytest.approx([0.2, 0.571, -1.857], abs=EPSILON)]


def test_LUP_decomposition1():
    matrix = Matrix([[3,2,1],[1,2,2],[4,3,4]])

    assert LUP_decomposition(matrix)[0].matrix == [[4, 3, 4], [1 / 4, 5 / 4, 1], [3 / 4, -1 / 5, -9 / 5]]


def test_matrix_inverse():
    matrix = Matrix([[4, 7], [2, 6]])

    assert matrix_inverse(matrix).matrix == [pytest.approx([0.6, -0.7], abs=EPSILON),
                                             pytest.approx([-0.2, 0.4], abs=EPSILON)]


def test_pivot_choosing():
    matrix = [[4, 3, 2, 1], [4, 6, 1, -1], [-8, 3, -5, -6], [-12, 2, 7, -4]]

    assert choose_pivot_element(matrix, 0) == 0
    assert choose_pivot_element(matrix, 1) == 1
    assert choose_pivot_element(matrix, 2) == 3
    assert choose_pivot_element(matrix, 3) == 3


def test_determinant():
    matrix = Matrix([[4, 7], [2, 6]])

    assert matrix_determinant(matrix) == 10

    matrix = Matrix([[3,2,1],[1,2,2],[4,3,4]])

    assert matrix_determinant(matrix) == 9

    matrix = Matrix([[4, 3, 2, 1], [4, 6, 1, -1], [-8, 3, -5, -6], [12, 12, 7, 4]])

    assert matrix_determinant(matrix) == pytest.approx(24, abs=EPSILON)

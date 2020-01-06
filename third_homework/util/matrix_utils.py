from copy import deepcopy
from math import isclose

from third_homework.util.matrix import Matrix

EPSILON = 10e-6


def LUP_decomposition(matrix: Matrix):
    if not matrix.is_square():
        raise ValueError('The matrix must be a square matrix!')

    p = Matrix.eye_matrix(matrix.rows)

    matrix_copy = deepcopy(matrix.matrix)

    permutation_counter = 0

    for i in range(matrix.rows):
        pivot = choose_pivot_element(matrix_copy, i)

        if isclose(matrix_copy[pivot][pivot], 0, abs_tol=EPSILON):
            raise PivotElementIsZero

        matrix_copy[pivot], matrix_copy[i] = matrix_copy[i], matrix_copy[pivot]
        p[i], p[pivot] = p[pivot], p[i]

        if i != pivot:
            permutation_counter += 1

        for j in range(i+1, matrix.rows):
            matrix_copy[j][i] /= matrix_copy[i][i]

            for k in range(i+1, matrix.rows):
                matrix_copy[j][k] -= matrix_copy[j][i] * matrix_copy[i][k]

    return Matrix(matrix_copy), p, permutation_counter


def choose_pivot_element(matrix, start_row):
    max_value = abs(matrix[start_row][start_row])

    pivot = start_row

    if start_row == len(matrix) - 1:
        return pivot

    for i in range(start_row + 1, len(matrix)):
        if abs(matrix[i][start_row]) > max_value:
            max_value = abs(matrix[i][start_row])
            pivot = i

    return pivot


def forward_substitution(matrix: Matrix, vector: Matrix) -> Matrix:
    if not matrix.is_square() or vector.cols != matrix.cols:
        raise ValueError('The vector must be of the same size as the quadrant matrix!')

    result = vector[0]

    for i in range(matrix.rows - 1):
        for j in range(i + 1, matrix.rows):
            result[j] -= matrix[j][i] * result[i]

    return Matrix([result])


def backward_substitution(matrix: Matrix, vector: Matrix) -> Matrix:
    if not matrix.is_square() or vector.cols != matrix.cols:
        raise ValueError('The vector must be of the same size as the quadrant matrix!')

    result = vector[0]

    for i in reversed(range(matrix.rows)):
        result[i] /= matrix[i][i]
        for j in range(i):
            result[j] -= matrix[j][i] * result[i]

    return Matrix([result])


def solve_equation(matrix: Matrix, vector: Matrix):
    LU_matrix, permutation_matrix, _ = LUP_decomposition(matrix)

    y = forward_substitution(LU_matrix, Matrix(Matrix(permutation_matrix) * vector).transpose)
    x = backward_substitution(LU_matrix, y)

    return x


def matrix_inverse(matrix: Matrix):
    LU_matrix, permutation_matrix, _ = LUP_decomposition(matrix)

    permutation_matrix_transposed = [list(x) for x in zip(*permutation_matrix)]

    inverse_matrix = []

    for i in range(matrix.rows):
        pi = permutation_matrix_transposed[i]

        yi = forward_substitution(LU_matrix, Matrix([pi]))
        xi = backward_substitution(LU_matrix, yi)

        inverse_matrix.append(xi.matrix[0])

    return Matrix(inverse_matrix).transpose


class PivotElementIsZero(BaseException):
    def __str__(self):
        return 'pivot element is zero'

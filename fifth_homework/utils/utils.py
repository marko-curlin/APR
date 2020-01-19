from typing import List
from math import sqrt, log

from fifth_homework.utils.matrix import Matrix
from fifth_homework.utils.matrix_utils import matrix_inverse as _matrix_inverse


def norm(vector: List[float]) -> float:
    return sqrt(sum([x**2 for x in vector]))


def multiply_each_element(vector: List[float], x: float) -> List[float]:
    return [x * element for element in vector]


def multiply_each_element_of_matrix(matrix: List[List[float]], x: float) -> List[List[float]]:
    multiplied_matrix = []
    for row in matrix:
        multiplied_matrix.append(multiply_each_element(row, x))
    return multiplied_matrix


def add_elements_on_same_index(vector1: List[float], vector2: List[float]) -> List[float]:
    return [el1 + el2 for el1, el2 in zip(vector1, vector2)]


def add_elements_on_same_index_of_matrix(matrix1: List[List[float]], matrix2: List[List[float]]) -> List[List[float]]:
    summed_matrix = []
    for row1, row2 in zip(matrix1, matrix2):
        summed_matrix.append(add_elements_on_same_index(row1, row2))
    return summed_matrix


def sub_elements_on_same_index(vector1: List[float], vector2: List[float]) -> List[float]:
    return [el1 - el2 for el1, el2 in zip(vector1, vector2)]


def mul_elements_on_same_index(vector1: List[float], vector2: List[float]) -> List[float]:
    return [el1 * el2 for el1, el2 in zip(vector1, vector2)]


def max_diff_on_same_indices(vector1: List[float], vector2: List[float]) -> float:
    return max(map(abs, sub_elements_on_same_index(vector1, vector2)))


def frange(start, stop=None, step=None):
    # if stop and step argument is None set start=0.0 and step = 1.0
    start = float(start)
    if stop is None:
        stop = start + 0.0
        start = 0.0
    if step is None:
        step = 1.0

    count = 0
    while True:
        temp = float(start + count * step)
        if step > 0 and temp >= stop + step:
            break
        elif step < 0 and temp <= stop + step:
            break
        yield temp
        count += 1


def create_eye_matrix(n):
    eye_matrix = []
    for i in range(n):
        current_row = [0] * n
        current_row[i] = 1
        eye_matrix.append(current_row)
    return eye_matrix


def multiply_matrices(a, b):
    zip_b = zip(*b)
    zip_b = list(zip_b)
    return [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b))
             for col_b in zip_b] for row_a in a]


def matrix_inverse(matrix: List[List[float]]) -> List[List[float]]:
    return _matrix_inverse(Matrix(matrix)).as_list()

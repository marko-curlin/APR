from copy import deepcopy
from math import isclose


def check_matrix(matrix):
    """
    Check if matrix is a proper matrix
    """
    if not matrix:
        raise ValueError("Matrix can't be None")
    try:
        cols = len(matrix[0])
    except IndexError:
        raise ValueError('Matrix has to have at least one row')
    for row in matrix[1:]:
        if len(row) != cols:
            raise ValueError('All rows must have the same number of columns')


def check_is_number(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool)


class Matrix:

    def __init__(self, matrix=[[]]):
        self._init_from_list(matrix)

    def _init_from_list(self, matrix=[[]]):
        check_matrix(matrix)
        if not isinstance(matrix[0], list):
            self.matrix = [matrix]
        self.matrix = matrix

    @property
    def rows(self):
        return len(self.matrix)

    @property
    def cols(self):
        return len(self.matrix[0])


    def print_matrix(self):
        for row in self.matrix:
            for col in row:
                if abs(col) < 10e-9:
                    print('0 ', end='')
                else:
                    print("{:.4}".format(col) + ' ', end='')
            print()

    def print_matrix_to_file(self, output_file_location: str):
        with open(output_file_location, 'w') as output_file:
            for row in self.matrix:
                for col in row:
                    output_file.write(str(col) + ' ')
                output_file.write('\n')

    def __getitem__(self, index):
        # if self.rows == 1:
        #     return self.matrix[0][index]

        return self.matrix[index]

    def __setitem__(self, index, x):    # TODO: make it work with 2D assignment
        if isinstance(x, (tuple, list)):
            if len(x) == self.cols:
                self.matrix[index] = x
                return
            else:
                raise ValueError('Rows must be replaced with rows of same length!')

        if not check_is_number(x):
            raise ValueError('Matrix element must be a real number')
        else:
            self.matrix[index] = x

        # if index >= len(self):
        #     self.vector.extend(index + 1)
        # self.vector[index] = item

    def __iadd__(self, other):
        if other.rows != self.rows or other.cols != self.cols:
            raise ValueError('The matrices must be of the same dimensions!')

        for i in range(self.rows):
            for j in range(self.cols):
                self[i][j] += other[i][j]

        return self

    def __add__(self, other):
        if other.rows != self.rows or other.cols != self.cols:
            raise ValueError('The matrices must be of the same dimensions!')

        tmp_matrix = deepcopy(self.matrix)

        for i in range(self.rows):
            for j in range(self.cols):
                tmp_matrix += other[i][j]

        return tmp_matrix

    def __sub__(self, other):
        if other.rows != self.rows or other.cols != self.cols:
            raise ValueError('The matrices must be of the same dimensions!')

        tmp_matrix = deepcopy(self.matrix)

        for i in range(self.rows):
            for j in range(self.cols):
                tmp_matrix -= other[i][j]

        return tmp_matrix

    def __isub__(self, other):
        if other.rows != self.rows or other.cols != self.cols:
            raise ValueError('The matrices must be of the same dimensions!')

        for i in range(self.rows):
            for j in range(self.cols):
                self[i][j] -= other[i][j]

        return self

    def __mul__(self, other):
        if check_is_number(other):
            return self.multiply_with_scalar(other)

        if isinstance(other, (Matrix, list)):
            return self.multiply_with_matrix(other)

        raise ValueError('Multiplication has to be with a matrix or number')

    def __imul__(self, other):
        self.matrix = self * other
        return self

    def __eq__(self, other):
        if other.rows != self.rows or other.cols != self.cols:
            return False

        for i in range(self.rows):
            for j in range(self.cols):
                if not isclose(self[i][j], other[i][j]):
                    return False

        return True

    def multiply_with_scalar(self, other):
        if not check_is_number(other):
            raise ValueError('The scalar must be a real number!')

        result = []

        for i in range(self.rows):
            result_row = []

            for j in range(self.cols):
                result_row.append(self[i][j] * other)

            result.append(result_row)

        return result

    @property
    def transpose(self):
        # self.matrix = list(zip(*self.matrix)) -> turns rows into tuples!!

        transposed_matrix = []

        for j in range(self.cols):
            transposed_row = []

            for i in range(self.rows):
                transposed_row.append(self.matrix[i][j])

            transposed_matrix.append(transposed_row)

        return Matrix(transposed_matrix)

    def multiply_with_matrix(self, other):
        if not isinstance(other, (Matrix, list)):
            raise ValueError('The other variable must be a matrix')

        if self.cols != other.rows:
            raise ValueError('The other matrix must have the same number of rows as this matrix has columns!')

        result = []

        for i in range(self.rows):
            result_row = []

            for j in range(other.cols):
                result_col_value = 0

                for k in range(self.cols):
                    result_col_value += self[i][k] * other[k][j]

                result_row.append(result_col_value)

            result.append(result_row)

        return result

    def is_square(self):
        return self.cols == self.rows

    @classmethod
    def eye_matrix(cls, n: int):
        eye_matrix = []

        for i in range(n):
            row = []

            for j in range(n):
                if j == i:
                    row.append(1)
                else:
                    row.append(0)

            eye_matrix.append(row)

        return eye_matrix

    def switch_columns(self, k, r):
        self.matrix = self.transpose.matrix

        self[k], self[r] = self[r], self[k]

        self.matrix = self.transpose.matrix

    def as_list(self):
        return self.matrix


if __name__ == '__main__':
    test_matrix = Matrix([[1.01, 2.1], [3, 4]])
    test_matrix[0] = [1, 2]

    assert test_matrix.matrix == [[1, 2], [3, 4]]

    test_matrix = Matrix([[0, 1]])
    test_matrix = test_matrix.transpose

    assert test_matrix.matrix == [[0], [1]]

    assert test_matrix == deepcopy(test_matrix)

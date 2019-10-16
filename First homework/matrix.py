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

def read_matrix_from_file(path_to_file: str):
    with open(path_to_file, 'r') as input_file:
        matrix = []

        for row in input_file:
            col_list = []
            cols = row.split()

            for col in cols:
                col_list.append(col)

            matrix.append(col_list)

    return matrix


class Matrix:

    def __init__(self, matrix=(())):
        if isinstance(matrix, (list, tuple)):
            self._init_from_list(matrix)
        if isinstance(matrix, str):
            self._init_from_file(matrix)

    def _init_from_list(self, matrix=(())):
        check_matrix(matrix)
        self.matrix = matrix
        # self.rows = len(matrix)
        # self.cols = len(matrix[0])

    @property
    def rows(self):
        return len(self.matrix)

    @property
    def cols(self):
        return len(self.matrix[0])

    def _init_from_file(self, path_to_file: str):
        matrix = read_matrix_from_file(path_to_file)
        self._init_from_list(matrix)

    def print_matrix(self):
        for row in self.matrix:
            for col in row:
                print(str(col) + ' ', end='')
            print()

    def print_matrix_to_file(self, output_file_location: str):
        with open(output_file_location, 'w') as output_file:
            for row in self.matrix:
                for col in row:
                    output_file.write(str(col) + ' ')
                output_file.write('\n')

    def __getitem__(self, index):
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
        if not check_is_number(other):
            raise ValueError('The scalar must be a real number!')

        for i in range(self.rows):
            for j in range(self.cols):
                self[i][j] *= other

        return self

    def __eq__(self, other):
        if other.rows != self.rows or other.cols != self.cols:
            return False

        for i in range(self.rows):
            for j in range(self.cols):
                if not isclose(self[i][j], other[i][j]):
                    return False

        return True

    def transpose(self):
        transposed_matrix = list()

        for j in range(self.cols):
            transposed_row = []

            for i in range(self.rows):
                transposed_row.append(self.matrix[i][j])

            transposed_matrix.append(transposed_row)

        self.matrix = transposed_matrix

    def multiply_matrices(self, other):
        

if __name__ == '__main__':
    # matrix = Matrix([[1.01,2.1], [3,4]])
    # matrix.print_matrix()
    # matrix[0] = [1,2]
    # matrix.print_matrix()

    matrix = Matrix([[0,1],[2,3],[4,5]])
    matrix.transpose()
    # matrix1 = Matrix([[0,1],[2,3.000000000001]])
    # matrix -= matrix1
    matrix.print_matrix()
    # print(matrix == matrix1)

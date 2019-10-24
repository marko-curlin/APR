from first_homework.matrix import Matrix


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

    for i in range(matrix.rows)[::-1]:
        result[i] /= matrix[i][i]
        for j in range(i):
            result[j] -= matrix[j][i] * result[i]

    return Matrix([result])


def LU_decomposition(matrix: Matrix) -> Matrix:
    if not matrix.is_square():
        raise ValueError('The matrix must be a square matrix!')

    LU_matrix = matrix.matrix

    for i in range(matrix.cols - 1):
        for j in range(i+1, matrix.rows):
            LU_matrix[j][i] /= LU_matrix[i][i]
            for k in range(i+1, matrix.rows):
                LU_matrix[j][k] -= LU_matrix[j][i] * LU_matrix[i][k]

    return Matrix(LU_matrix)


def LUP_decomposition(matrix: Matrix):
    if not matrix.is_square():
        raise ValueError('The matrix must be a square matrix!')

    p = Matrix.eye_matrix(matrix.rows)

    for i in range(matrix.rows):
        pass


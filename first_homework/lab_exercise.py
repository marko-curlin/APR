from math import pi, sqrt

from first_homework.solution import *


def first_task():
    matrix = Matrix([[1.1, 2.2]])

    assert matrix[0][0] == 1.1
    assert matrix[0][1] == 2.2

    matrix *= pi * sqrt(10)
    matrix *= 1 / pi / sqrt(10)

    assert matrix[0][0] == 1.1
    assert matrix[0][1] == 2.2


def second_task(LUP_flag):
    matrix = Matrix([[3,9,6], [4,12,12], [1,-1,1]])
    vector = Matrix([[12,12,1]]).transpose

    try:
        x = solve_equation(matrix, vector, LUP_flag)
    except ZeroDivisionError as e:
        print(e)
        return
    except PivotElementIsZero as e:
        print(e)
        return

    x.transpose.print_matrix()


def solve_equation(matrix: Matrix, vector: Matrix, LUP_decomposition_flag: bool):
    if LUP_decomposition_flag:
        LU_matrix, permutation_matrix, _ = LUP_decomposition(matrix)
    else:
        LU_matrix, permutation_matrix, _ = LU_decomposition(matrix)

    y = forward_substitution(LU_matrix, Matrix(Matrix(permutation_matrix) * vector).transpose)
    x = backward_substitution(LU_matrix, y)

    return x


def third_task(LUP_flag):
    matrix = Matrix([[1,2,3], [4,5,6], [7,8,9]])
    vector = Matrix([[12,12,1]]).transpose

    try:
        x = solve_equation(matrix, vector, LUP_flag)
    except ZeroDivisionError as e:
        print(e)
        return
    except PivotElementIsZero as e:
        print(e)
        return

    x.transpose.print_matrix()


def fourth_task(LUP_flag):
    matrix = Matrix([[0.000001, 3_000_000, 2_000_000], [1_000_000, 2_000_000, 3_000_000], [2_000_000, 1_000_000, 2_000_000]])
    vector = Matrix([[12_000_000.000001, 14_000_000, 10_000_000]]).transpose

    try:
        x = solve_equation(matrix, vector, LUP_flag)
    except ZeroDivisionError as e:
        print(e)
        return
    except PivotElementIsZero as e:
        print(e)
        return

    x.transpose.print_matrix()


def fifth_task(LUP_flag):
    matrix = Matrix([[0,1,2], [2,0,3], [3,5,1]])
    vector = Matrix([[6,9,3]]).transpose

    try:
        x = solve_equation(matrix, vector, LUP_flag)
    except ZeroDivisionError as e:
        print(e)
        return
    except PivotElementIsZero as e:
        print(e)
        return

    x.transpose.print_matrix()


def sixth_task(LUP_flag):
    matrix = Matrix([[4_000_000_000, 1_000_000_000, 3_000_000_000], [4, 2, 7], [0.000_000_000_3, 0.000_000_000_5, 0.000_000_000_2]])
    vector = Matrix([[9_000_000_000, 15, 0.000_000_000_15]]).transpose

    try:
        x = solve_equation(matrix, vector, LUP_flag)
    except ZeroDivisionError as e:
        print(e)
        return
    except PivotElementIsZero as e:
        print(e)
        return

    x.transpose.print_matrix()


def seventh_task():
    matrix = Matrix([[1,2,3], [4,5,6], [7,8,9]])

    try:
        matrix_inverse(matrix).print_matrix()
    except PivotElementIsZero as e:
        print(e)
        return


def eight_task():
    matrix = Matrix([[4,-5,-2], [5,-6,-2], [-8,9,3]])

    try:
        matrix_inverse(matrix).print_matrix()
    except PivotElementIsZero as e:
        print(e)
        return


def ninth_task():
    matrix = Matrix([[4,-5,-2], [5,-6,-2], [-8,9,3]])

    print('determinant = ' + str(matrix_determinant(matrix)))


def tenth_task():
    matrix = Matrix([[3,9,6], [4,12,12], [1,-1,1]])

    print('determinant = ' + str(matrix_determinant(matrix)))


if __name__ == '__main__':
    first_task()

    print('DRUGI ZADATAK:')
    print('LUP:')
    second_task(True)
    print('LU:')
    second_task(False)
    print('\n')

    print('TREĆI ZADATAK:')
    print('LUP:')
    third_task(True)
    print('LU:')
    third_task(False)
    print('\n')

    print('ČETVRTI ZADATAK')
    print('LUP:')
    fourth_task(True)
    print('LU:')
    fourth_task(False)
    print('\n')

    print('PETI ZADATAK')
    print('LUP:')
    fifth_task(True)
    print('LU:')
    fifth_task(False)
    print('\n')

    print('ŠESTI ZADATAK')
    print('LUP:')
    sixth_task(True)
    print('LU:')
    sixth_task(False)
    print('\n')

    print('ŠESTI ZADATAK')
    print('LUP:')
    sixth_task(True)
    print('LU:')
    sixth_task(False)
    print('\n')

    print('SEDMI ZADATAK:')
    seventh_task()
    print('\n')

    print('OSMI ZADATAK:')
    eight_task()
    print('\n')

    print('DEVETI ZADATAK:')
    ninth_task()
    print('\n')

    print('DESETI ZADATAK:')
    tenth_task()

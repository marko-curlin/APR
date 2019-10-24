from first_homework.solution import *


def backward_substitution1():
    matrix = Matrix([[2, 2, 3], [2, 3, 0], [0, 4, 2]])
    vector = Matrix([[25, -15, 75]])

    assert backward_substitution(matrix, vector).matrix == [[5, 0, 5]]


def backward_substitution2():
    matrix = Matrix([[5, 6, 3], [0, 1.4, 2.2], [0, 0, -1.856]])
    vector = Matrix([[10.3, 6.32, -5.569]])

    assert backward_substitution(matrix, vector).matrix == [[0.5, -0.2, 3]]


def test_forward_substitution3():
    matrix = Matrix([[1, 0, 0], [1/3, 1, 0], [0, 12/7, 0]])
    vector = Matrix([[2, 3, 4]])

    assert forward_substitution(matrix, vector).matrix == [[2, 7/3, 0]]


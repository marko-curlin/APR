from fifth_homework.algorithms.top_algorithm import TopAlgorithm
from fifth_homework.utils.utils import *


class ReverseEulerMethod(TopAlgorithm):
    def __init__(self,
                 A,
                 B,
                 r_functions,
                 x_0,
                 T,
                 t_max,
                 print_after_iteration
                 ):
        super().__init__(A, B, r_functions, x_0, T, t_max, print_after_iteration)

        U = create_eye_matrix(len(A))

        self.P = matrix_inverse(add_elements_on_same_index_of_matrix(U, multiply_each_element_of_matrix(A, -T)))

        self.Q = multiply_matrices(multiply_each_element_of_matrix(self.P, T), B) if B is not None else None

    def find_next(self, x_k, t_k) -> List[float]:
        _next = multiply_matrices(self.P, x_k)

        if self.Q is not None:
            t_k_1 = t_k + self.T
            _next = add_elements_on_same_index_of_matrix(_next, multiply_matrices(self.Q, self.get_r_matrix(t_k_1)))

        return add_elements_on_same_index(x_k, multiply_each_element(_next[0], self.T))

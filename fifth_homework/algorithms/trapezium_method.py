from fifth_homework.algorithms.top_algorithm import TopAlgorithm
from fifth_homework.utils.utils import *


class TrapeziumMethod(TopAlgorithm):
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

        U_sub_A_half_T_inv = matrix_inverse(add_elements_on_same_index_of_matrix(U, multiply_each_element_of_matrix(A, -T/2)))
        U_add_A_half_T = add_elements_on_same_index_of_matrix(U, multiply_each_element_of_matrix(A, T/2))

        self.R = multiply_matrices(U_sub_A_half_T_inv, U_add_A_half_T)

        self.S = multiply_matrices(multiply_each_element_of_matrix(U_sub_A_half_T_inv, T/2), B) if B is not None else None

    def find_next(self, x_k, t_k) -> List[float]:
        _next = multiply_matrices(self.R, x_k)

        if self.S is not None:
            t_k_1 = t_k + self.T

            sum_of_r_matrices = add_elements_on_same_index_of_matrix(self.get_r_matrix(t_k), self.get_r_matrix(t_k_1))

            _next = add_elements_on_same_index_of_matrix(_next, multiply_matrices(self.S, sum_of_r_matrices))

        return _next[0]

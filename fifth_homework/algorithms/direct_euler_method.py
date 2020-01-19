from fifth_homework.algorithms.top_algorithm import TopAlgorithm
from fifth_homework.utils.utils import *


class DirectEulerMethod(TopAlgorithm):
    def __init__(self, T, t_max, A, x_0, B=None, r_functions=None, print_after_iteration=10):
        super().__init__(T, t_max, A, x_0, B, r_functions, print_after_iteration)

        U = create_eye_matrix(len(A))

        self.M = add_elements_on_same_index_of_matrix(U, multiply_each_element_of_matrix(A, T))

        self.N = multiply_each_element_of_matrix(B, T) if B is not None else None

    def find_next(self, x_k, t_k) -> List[float]:
        _next = multiply_matrices(self.M, x_k)

        if self.N is not None:
            N_mul_r = multiply_matrices(self.N, self.get_r_matrix(t_k))

            _next = add_elements_on_same_index_of_matrix(_next, N_mul_r)

        return _next[0]

    def predict(self, x_k, t_k):
        return self.find_next(x_k, t_k)

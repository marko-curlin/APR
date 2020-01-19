from fifth_homework.algorithms.top_algorithm import TopAlgorithm
from fifth_homework.utils.utils import *


class RungeKuttaMethod(TopAlgorithm):
    def __init__(self, T, t_max, A, x_0, B=None, r_functions=None, print_after_iteration=100):
        super().__init__(T, t_max, A, x_0, B, r_functions, print_after_iteration)

    def find_next(self, x_k, t_k) -> List[float]:
        m_1 = multiply_matrices(self.A, x_k)
        if self.B is not None:
            m_1 = add_elements_on_same_index(m_1, multiply_matrices(self.B, self.get_r_matrix(t_k)))

        m_2 = self.get_first_addend(x_k, m_1, 1/2)
        if self.B is not None:
            m_2 = add_elements_on_same_index(m_2, self.get_second_addend(t_k, 1/2))

        m_3 = self.get_first_addend(x_k, m_2, 1/2)
        if self.B is not None:
            m_3 = add_elements_on_same_index(m_3, self.get_second_addend(t_k, 1/2))

        m_4 = self.get_first_addend(x_k, m_3, 1)
        if self.B is not None:
            m_4 = add_elements_on_same_index(m_4, self.get_second_addend(t_k, 1))

        _next = add_elements_on_same_index(x_k, multiply_each_element(add_vectors(m_1, multiply_each_element(m_2, 2), multiply_each_element(m_3, 2), m_4), self.T/6))

        return _next

    def get_first_addend(self, x_k, m, mul):
        return multiply_matrices(self.A, add_elements_on_same_index(x_k, multiply_each_element(m, mul*self.T)))

    def get_second_addend(self, t_k, mul):
        if self.B is None:
            return [0] * self.x_0

        return multiply_matrices(self.B, self.get_r_matrix(t_k + self.T * mul))

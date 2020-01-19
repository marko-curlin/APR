from abc import ABC, abstractmethod
from prettytable import PrettyTable

from fifth_homework.utils.utils import *


class TopAlgorithm(ABC):
    def __init__(self, T, t_max, A, x_0, B=None, r_functions=None, print_after_iteration=100):
        self.A = A
        self.B = B
        self.r_functions = r_functions
        self.x_0 = x_0
        self.T = T
        self.t_max = t_max
        self.print_after_iteration = print_after_iteration

    def solve_equation(self):
        table = PrettyTable(['iteration', 'tk', 'xK', 'xK+1'])
        x_k = self.x_0

        x = [x_k]

        iteration = 1
        for t_k in frange(self.T, self.t_max, self.T):
            x_k_1 = self.find_next(x_k, t_k)
            x.append(x_k_1)

            if iteration % self.print_after_iteration == 0:
                table.add_row([iteration, round(t_k, 1), x_k, x_k_1])

            x_k = x_k_1
            iteration += 1

        print(table)

        return x

    def get_r_matrix(self, t):
        r_matrix = []

        for function in self.r_functions:
            r_matrix.append([function(t)])

        return r_matrix

    @abstractmethod
    def find_next(self, x_k, t_k):
        pass

from copy import deepcopy
from typing import Callable

from third_homework.limits.implicit_limits import ImplicitLimit
from third_homework.util.utils import *


class Function:
    def __init__(self, func):
        self.func = func
        self.nr_of_calls = 0
        self.previous_results = {}
        self.total_nr_of_calls = 0
        self.gradient_calls = 0
        self.Hesse_matrix_calls = 0

    def __call__(self, *x):
        self.total_nr_of_calls += 1

        if x in self.previous_results:
            return self.previous_results[x]

        result = self.preform_function(x)

        self.previous_results[x] = result

        self.nr_of_calls += 1

        return result

    def preform_function(self, x):
        return self.func(*x)

    def calculate_gradient(self, *x):
        self.gradient_calls += 1
        return self._calculate_gradient(*x)

    def _calculate_gradient(self, *x):
        raise NotImplementedError

    def calculate_hesse_matrix(self, *x):
        self.Hesse_matrix_calls += 1
        return self._calculate_hesse_matrix(*x)

    def _calculate_hesse_matrix(self, *x):
        raise NotImplementedError


class LambdaFunction(Function):
    def __init__(self, func, vector, gradient):
        super().__init__(func)
        self.vector = deepcopy(vector)
        self.gradient = deepcopy(gradient)

    def __call__(self, x):
        self.total_nr_of_calls += 1

        vector_with_lambda = deepcopy(self.vector)
        vector_with_lambda = add_elements_on_same_index(vector_with_lambda, multiply_each_element(self.gradient, x))

        vector_with_lambda = tuple(vector_with_lambda)

        if vector_with_lambda in self.previous_results:
            return self.previous_results[vector_with_lambda]

        result = self.func(*vector_with_lambda)

        self.previous_results[vector_with_lambda] = result

        self.nr_of_calls += 1

        return result


class InnerPointFunction(Function):
    def __init__(self, implicit_limits: List[ImplicitLimit]):
        super().__init__(None)
        self.implicit_limits = implicit_limits

    def preform_function(self, x):
        _sum = 0
        for limit in self.implicit_limits:
            value = limit.get_value(*x)
            if value < 0:
                _sum += limit.get_value(*x)
        return multiply_each_element(_sum, -1)
        # return sum([-limit.get_value(*x) if limit.get_value(*x) < 0 else 0 for limit in self.implicit_limits])

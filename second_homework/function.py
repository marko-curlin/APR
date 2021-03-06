from copy import deepcopy


# class _OneVariableFunction:
#     def __init__(self, func):
#         self.func = func
#         self.nr_of_calls = 0
#         self.previous_results = {}
#         self.total_nr_of_calls = 0
#
#     def __call__(self, x):
#         self.total_nr_of_calls += 1
#
#         if x in self.previous_results:
#             return self.previous_results[x]
#
#         result = self.func(x)
#
#         self.previous_results[x] = result
#
#         self.nr_of_calls += 1
#
#         return result
#
#
# class _MultiVariableFunction:
#     def __init__(self, func):
#         self.func = func
#         self.nr_of_calls = 0
#         self.previous_results = {}
#         self.total_nr_of_calls = 0
#
#     def __call__(self, *x):
#         self.total_nr_of_calls += 1
#
#         if x in self.previous_results:
#             return self.previous_results[x]
#
#         result = self.func(*x)
#
#         self.previous_results[x] = result
#
#         self.nr_of_calls += 1
#
#         return result


class Function:
    def __init__(self, func):
        self.func = func
        self.nr_of_calls = 0
        self.previous_results = {}
        self.total_nr_of_calls = 0

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


class LambdaFunction(Function):
    def __init__(self, func, vector, current_index):
        super().__init__(func)
        self.vector = deepcopy(vector)
        self.current_index = current_index

    def __call__(self, x):
        self.total_nr_of_calls += 1

        vector_with_lambda = deepcopy(self.vector)
        vector_with_lambda[self.current_index] += x

        vector_with_lambda = tuple(vector_with_lambda)

        if vector_with_lambda in self.previous_results:
            return self.previous_results[vector_with_lambda]

        result = self.func(*vector_with_lambda)

        self.previous_results[vector_with_lambda] = result

        self.nr_of_calls += 1

        return result

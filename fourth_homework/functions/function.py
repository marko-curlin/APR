from typing import Callable


class Function:
    def __init__(self, func: Callable):
        self.func = func
        self.previous_results = {}

    def __call__(self, *x):
        # if x in self.previous_results:
        #     return self.previous_results[x]

        result = self.preform_function(x)

        # self.previous_results[x] = result

        return result

    def preform_function(self, x):
        return self.func(*x)


class FitnessFunction:
    def __init__(self, func: Callable):
        self.func = func

    def __call__(self, *point):
        return -self.func(*point)

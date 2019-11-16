from copy import deepcopy


class OneVariableFunction:
    def __init__(self, func):
        self.func = func
        self.nr_of_calls = 0
        self.previous_results = {}
        self.total_nr_of_calls = 0

    def __call__(self, x):
        self.total_nr_of_calls += 1

        if x in self.previous_results:
            return self.previous_results[x]

        result = self.func(x)

        self.previous_results[x] = result

        self.nr_of_calls += 1

        return result


class LambdaFunction(OneVariableFunction):
    def __init__(self, func, current_vector, current_index):
        super().__init__(func)
        self.vector = deepcopy(current_vector)
        self.current_index = current_index

    def __call__(self, x):  # refactor so previous result is used correctly
        self.total_nr_of_calls += 1

        # if x in self.previous_results:
        #     return self.previous_results[x]

        vector = deepcopy(self.vector)
        vector[self.current_index] += x

        result = self.func(*vector)

        self.previous_results[x] = result

        self.nr_of_calls += 1

        return result

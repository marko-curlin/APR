from fifth_homework.algorithms.top_algorithm import TopAlgorithm
from fifth_homework.utils.utils import *


class PredictorCorrectorMethod(TopAlgorithm):
    def __init__(self, explicit_method_class, implicit_method_class, T, t_max, s, A, x_0, B=None, r_functions=None, print_after_iteration=100):
        super().__init__(T, t_max, A, x_0, B, r_functions, print_after_iteration)

        self.predictor = explicit_method_class(T, t_max, A, x_0, B, r_functions, print_after_iteration)
        self.corrector = implicit_method_class(T, t_max, A, x_0, B, r_functions, print_after_iteration)

        self.s = s

    def find_next(self, x_k, t_k) -> List[float]:
        _next = self.predictor.predict(x_k, t_k)

        for _ in range(self.s):
            _next = self.corrector.correct(x_k, _next, t_k)

        return _next

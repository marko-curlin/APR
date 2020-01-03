from .function import Function


class FirstFunction(Function):
    def __init__(self):
        super().__init__(lambda x, y: 100 * (y - x**2) + (1 - x)**2)

    def _calculate_gradient(self, *x):
        return [400 * x[0] * (x[0]**2 - x[1]) + 2 * x[0] - 2, -200 * x[0]**2 + 200 * x[1]]

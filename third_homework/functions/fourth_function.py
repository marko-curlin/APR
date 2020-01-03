from .function import Function


class FourthFunction(Function):
    def __init__(self):
        super().__init__(lambda x, y: (x - 3)**2 + y**2)

    def _calculate_gradient(self, *x):
        return 2 * (x[0] - 3), 2 * x[1]

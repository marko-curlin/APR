from .function import Function


class ThirdFunction(Function):
    def __init__(self):
        super().__init__(lambda x, y: (x - 2)**2 + (y + 3)**2)

    def _calculate_gradient(self, *x):
        return 2 * (x[0] - 2), 2 * (x[1] + 3)

from .function import Function


class ThirdFunction(Function):
    def __init__(self):
        super().__init__(lambda x, y: (x - 2)**2 + (y + 3)**2)

    def _calculate_gradient(self, *x):
        return 2 * (x[0] - 2), 2 * (x[1] + 3)

    def _calculate_hesse_matrix(self, *x):
        derivation11 = 2
        derivation12 = 0
        derivation21 = 0
        derivation22 = 2

        return [[derivation11, derivation12], [derivation21, derivation22]]

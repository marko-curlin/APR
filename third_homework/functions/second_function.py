from .function import Function


class SecondFunction(Function):
    def __init__(self):
        super().__init__(lambda x, y: (x - 4)**2 + 4*(y - 2)**2)

    def _calculate_gradient(self, *x):
        return 2 * (x[0] - 4), 8 * (x[1] - 2)

    def _calculate_hesse_matrix(self, *x):
        derivation11 = 2
        derivation12 = 0
        derivation21 = 0
        derivation22 = 8

        return [[derivation11, derivation12], [derivation21, derivation22]]

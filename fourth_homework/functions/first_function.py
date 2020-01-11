from fourth_homework.functions.function import Function


class FirstFunction(Function):
    def __init__(self):
        super().__init__(lambda x, y: 100 * (y - x**2)**2 + (1 - x)**2)

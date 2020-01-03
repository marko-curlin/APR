from .first_function import FirstFunction
from .second_function import SecondFunction
from .third_function import ThirdFunction
from .fourth_function import FourthFunction


def get_function_and_start_point(i: int):
    if i == 1:
        return FirstFunction(), (-1.9, 2)
    if i == 2:
        return SecondFunction(), (0.1, 0.3)
    if i == 3:
        return ThirdFunction(), (0, 0)
    if i == 4:
        return FourthFunction(), (0, 0)

    raise ValueError('Function indexes are in the range [1, 4]!')

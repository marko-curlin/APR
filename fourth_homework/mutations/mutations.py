from random import random

from fourth_homework.float_unit import FloatUnit
from fourth_homework.utils import *

DIVISOR = 1000


class FloatMutationLocalShift:
    @staticmethod
    def mutate_unit(unit: FloatUnit, lower_limit, upper_limit):
        random_vector = [random() * (upper_limit - lower_limit) / DIVISOR for _ in range(unit.dimension)]
        random_vector = [-el if random() < 0.5 else el for el in random_vector]

        new_point = add_elements_on_same_index(unit.point, random_vector)
        new_point = set_within_limits(new_point, lower_limit, upper_limit)

        return FloatUnit(new_point)

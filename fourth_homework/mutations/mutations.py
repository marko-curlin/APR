from random import random

from fourth_homework.units import FloatUnit, BinaryUnit
from fourth_homework.utils import *

DIVISOR = 1000


class FloatMutationLocalShift:
    @staticmethod
    def mutate_unit(unit: FloatUnit, lower_limit, upper_limit):
        random_vector = [random() * (upper_limit - lower_limit) / DIVISOR for _ in range(unit.dimension)]
        random_vector = [-el if random() < 0.5 else el for el in random_vector]

        new_point = add_elements_on_same_index(unit.real_point, random_vector)
        new_point = set_within_limits(new_point, lower_limit, upper_limit)

        return FloatUnit(new_point)


class BinarySimpleMutation:
    @staticmethod
    def mutate_unit(unit: BinaryUnit, lower_limit, upper_limit):
        new_point: List[List[int]] = []

        for coordinate in unit.point:
            new_coordinate = []

            for i in coordinate:
                new_coordinate.append(i if random() < 0.5 else 1-i)

            new_point.append(new_coordinate)

        return BinaryUnit(new_point, lower_limit, upper_limit)

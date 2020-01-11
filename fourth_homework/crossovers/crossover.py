from statistics import mean
from random import randint

from fourth_homework.float_unit import FloatUnit


class FloatAveragingCrossover:
    @staticmethod
    def create_new_unit(*units):
        new_point = []

        for i in range(units[0].dimension):
            new_point.append(mean(map(lambda unit: unit.point[i], units)))

        return FloatUnit(new_point)


class FloatSingleCrossoverPoint:
    @staticmethod
    def create_new_unit(unit1: FloatUnit, unit2: FloatUnit):
        cross_value = randint(0, unit1.dimension)

        new_point = unit1.point[:cross_value] + unit2.point[cross_value:]

        return FloatUnit(new_point)



from statistics import mean
from random import randint, random
from typing import List

from fourth_homework.units import FloatUnit, BinaryUnit


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


class BinarySingleCrossoverPoint:
    @staticmethod
    def create_new_unit(unit1: BinaryUnit, unit2: BinaryUnit):
        new_point: List[List[int]] = []
        cross_value = randint(0, unit1.nr_of_bits)

        for i in range(unit1.dimension):
            new_coordinate = unit1.point[i][:cross_value] + unit2.point[i][cross_value:]
            new_point.append(new_coordinate)

        return BinaryUnit(new_point, unit1.lower_limit, unit1.lower_limit)


class BinaryUniformCrossover:
    @staticmethod
    def create_new_unit(unit1: BinaryUnit, unit2: BinaryUnit):
        new_point: List[List[int]] = []

        for i in range(unit1.dimension):
            new_coordinate = []

            for j in range(unit1.nr_of_bits):
                new_coordinate.append(unit1.point[i][j] if random() < 0.5 else unit2.point[i][j])

            new_point.append(new_coordinate)

        return BinaryUnit(new_point, unit1.lower_limit, unit1.upper_limit)

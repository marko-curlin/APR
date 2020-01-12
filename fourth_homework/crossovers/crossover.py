from statistics import mean
from random import randint, random
from typing import List, Tuple

from fourth_homework.units import FloatUnit, BinaryUnit


class FloatAveragingCrossover:
    @staticmethod
    def create_new_unit(*units: Tuple[FloatUnit]):
        new_point = []

        for i in range(units[0].dimension):
            new_point.append(mean(map(lambda unit: unit.real_point[i], units)))

        return FloatUnit(new_point)


class FloatSingleCrossoverPoint:
    @staticmethod
    def create_new_unit(unit1: FloatUnit, unit2: FloatUnit):
        cross_value = randint(0, unit1.dimension)

        new_point = unit1.real_point[:cross_value] + unit2.real_point[cross_value:]

        return FloatUnit(new_point)


class FloatUniformCrossover:
    @staticmethod
    def create_new_unit(unit1: FloatUnit, unit2: FloatUnit):
        new_point = []

        for i in range(unit1.dimension):
            new_point.append(unit1.real_point[i] if random < 0.5 else unit2.real_point[i])

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
    def create_new_unit1(unit1: BinaryUnit, unit2: BinaryUnit):
        new_point: List[List[int]] = []

        for i in range(unit1.dimension):
            new_coordinate = []

            for j in range(unit1.nr_of_bits):
                new_coordinate.append(unit1.point[i][j] if random() < 0.5 else unit2.point[i][j])

            new_point.append(new_coordinate)

        return BinaryUnit(new_point, unit1.lower_limit, unit1.upper_limit)

    @staticmethod
    def create_new_unit(*units: Tuple[BinaryUnit]):
        new_point: List[List[int]] = []

        for i in range(units[0].dimension):
            new_coordinate = []

            for j in range(units[0].nr_of_bits):
                new_coordinate.append(choose_single_byte_from_units(i, j, units))

            new_point.append(new_coordinate)

        return BinaryUnit(new_point, units[0].lower_limit, units[0].upper_limit)


def choose_single_byte_from_units(dimension, bit, units):
    prob_for_units = []
    for i in range(len(units) + 1):
        prob_for_units.append(i / len(units))

    random_value = random()

    for i in range(len(prob_for_units) - 1):
        if prob_for_units[i] <= random_value < prob_for_units[i+1]:
            return units[i].point[dimension][bit]

    raise LookupError('Something went wrong.')

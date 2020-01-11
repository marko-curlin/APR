from random import random, randint
from typing import List
from math import log2, ceil

from fourth_homework.units import FloatUnit, BinaryUnit


class FloatPopulation:
    def __init__(self, lower_limit, upper_limit, nr_of_variables, population_size):
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit
        self.nr_of_variables = nr_of_variables
        self.population_size = population_size

        self.population: List[FloatUnit] = self.create_population()

    def evaluate_population(self, fitness_function):
        for unit in self.population:
            unit.evaluate_unit(fitness_function)

    def append(self, unit):
        self.population.append(unit)

    def remove(self, unit):
        self.population.remove(unit)

    def pick_units_at_random(self, nr_of_units):
        indices = []

        while len(indices) < nr_of_units:
            index = randint(0, self.population_size - 1)
            while index in indices:
                index += 1
                index %= self.population_size
            indices.append(index)

        return [self.population[i] for i in indices]

    def create_population(self):
        population = []

        while len(population) < self.population_size:
            point = []

            for _ in range(self.nr_of_variables):
                point.append(self.lower_limit + random() * (self.upper_limit - self.lower_limit))

            unit = FloatUnit(point)

            if unit not in population:
                population.append(unit)

        return population

    def get_best_unit(self):
        return max(self.population, key=lambda unit: unit.value)


class BinaryPopulation:
    def __init__(self, lower_limit, upper_limit, nr_of_variables, population_size, decimal_precision):
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit
        self.nr_of_variables = nr_of_variables
        self.population_size = population_size
        self.__decimal_precision = decimal_precision

        self.nr_of_bits = self.calculate_nr_of_bits()

        self.population: List[BinaryUnit] = self.create_population()

    def calculate_nr_of_bits(self):
        values_per_index = 10**self.__decimal_precision
        total_possible_values = (self.upper_limit - self.lower_limit) * values_per_index + 1
        return ceil(log2(total_possible_values))

    def evaluate_population(self, fitness_function):
        for unit in self.population:
            unit.evaluate_unit(fitness_function)

    def append(self, unit):
        self.population.append(unit)

    def remove(self, unit):
        self.population.remove(unit)

    def pick_units_at_random(self, nr_of_units):
        indices = []

        while len(indices) < nr_of_units:
            index = randint(0, self.population_size - 1)
            while index in indices:
                index += 1
                index %= self.population_size
            indices.append(index)

        return [self.population[i] for i in indices]

    def create_population(self):
        population: List[BinaryUnit] = []

        while len(population) < self.population_size:
            point: List[List[int]] = []

            for _ in range(self.nr_of_variables):
                point.append(self.create_random_point())

            unit = BinaryUnit(point, self.lower_limit, self.upper_limit)

            if unit not in population:
                population.append(unit)

        return population

    def get_best_unit(self):
        return max(self.population, key=lambda unit: unit.value)

    # def create_random_unit(self):
    #     for _ in random(self.nr_of_variables):
    #         self.create_random_point()

    def create_random_point(self) -> List[int]:
        return [0 if random() < 0.5 else 1 for _ in range(self.nr_of_bits)]

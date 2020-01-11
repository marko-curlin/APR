from random import random, randint
from typing import List

from fourth_homework.float_unit import FloatUnit, BinaryUnit


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

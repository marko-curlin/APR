from random import random
from abc import ABC, abstractmethod

from fourth_homework.functions.function import FitnessFunction


class GA(ABC):
    def __init__(self,
                 population_size,
                 mutation,
                 mutation_prob,
                 crossover,
                 max_evaluations):
        self.population_size = population_size
        self.mutation = mutation
        self.mutation_prob = mutation_prob
        self.crossover = crossover
        self.max_evaluations = max_evaluations

    def find_function_min(self, function, nr_of_variables, lower_limit, upper_limit):
        fitness_function = FitnessFunction(function)
        population = self.create_population(lower_limit, upper_limit, nr_of_variables)
        population.evaluate_population(fitness_function)

        nr_of_evaluations = 1

        overall_best_unit = population.get_best_unit()

        while nr_of_evaluations < self.max_evaluations:
            random_units = population.pick_units_at_random(3)

            worst_unit = self.find_worst_unit(random_units)

            population.remove(worst_unit)
            random_units.remove(worst_unit)

            new_unit = self.crossover.create_new_unit(*random_units)

            if random() < self.mutation_prob:
                new_unit = self.mutation.mutate_unit(new_unit, lower_limit, upper_limit)

            new_unit.evaluate_unit(fitness_function)
            population.append(new_unit)

            currently_best_unit = population.get_best_unit()
            if currently_best_unit.value > overall_best_unit.value:
                overall_best_unit = currently_best_unit

            nr_of_evaluations += 1

        return overall_best_unit.real_point

    @abstractmethod
    def create_population(self, lower_limit, upper_limit, nr_of_variables):
        pass

    @staticmethod
    def find_worst_unit(units):
        worst_unit = None

        for unit in units:
            if worst_unit is None or unit.value < worst_unit.value:
                worst_unit = unit

        return worst_unit

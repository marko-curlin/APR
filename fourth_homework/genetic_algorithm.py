from random import random
from abc import ABC, abstractmethod

from prettytable import PrettyTable

from fourth_homework.functions.function import FitnessFunction


class GA(ABC):
    def __init__(self,
                 population_size,
                 mutation,
                 mutation_prob,
                 crossover,
                 max_evaluations,
                 tournament_size=3,
                 cut_off=-1e-6):
        self.population_size = population_size
        self.mutation = mutation
        self.mutation_prob = mutation_prob
        self.crossover = crossover
        self.max_evaluations = max_evaluations
        self.tournament_size = tournament_size
        self.cut_off = cut_off

    def find_function_min(self, function, nr_of_variables, lower_limit, upper_limit):
        table = PrettyTable(['nr_of_evaluations', 'best_unit', 'value_of_best_unit', 'population_fitness'])
        table.int_format = '17'

        fitness_function = FitnessFunction(function)
        population = self.create_population(lower_limit, upper_limit, nr_of_variables)
        population.evaluate_population(fitness_function)

        nr_of_evaluations = 1

        overall_best_unit = population.get_best_unit()

        table.add_row([nr_of_evaluations, overall_best_unit.real_point, overall_best_unit.value, population.population_fitness])
        print(table)
        while nr_of_evaluations < self.max_evaluations:
            random_units = population.pick_units_at_random(self.tournament_size)

            worst_unit = self.find_worst_unit(random_units)

            population.remove(worst_unit)
            random_units.remove(worst_unit)

            new_unit = self.crossover.create_new_unit(*random_units)

            if random() < self.mutation_prob:
                new_unit = self.mutation.mutate_unit(new_unit, lower_limit, upper_limit)

            new_unit.evaluate_unit(fitness_function)
            nr_of_evaluations += 1
            population.append(new_unit)

            currently_best_unit = population.get_best_unit()
            if currently_best_unit.value > overall_best_unit.value:
                overall_best_unit = currently_best_unit

            if nr_of_evaluations % 50_000 == 0:
                table.add_row([nr_of_evaluations, overall_best_unit.real_point, overall_best_unit.value, population.population_fitness])
                print(table.get_string(header=False, start=table.rowcount-1, end=table.rowcount))

            if overall_best_unit.value > self.cut_off:
                break

        # print(table)
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

from fourth_homework.functions.first_function import FirstFunction
from fourth_homework.genetic_algorithm import GA
from fourth_homework.populations import BinaryPopulation
from fourth_homework.crossovers.crossover import BinaryUniformCrossover
from fourth_homework.mutations.mutations import BinarySimpleMutation


class GABinary(GA):
    def __init__(self,
                 population_size,
                 mutation,
                 mutation_prob,
                 crossover,
                 max_evaluations,
                 decimal_precision):
        super().__init__(population_size, mutation, mutation_prob, crossover, max_evaluations)
        self.decimal_precision = decimal_precision

    def create_population(self, lower_limit, upper_limit, nr_of_variables):
        return BinaryPopulation(lower_limit, upper_limit, nr_of_variables, self.population_size, self.decimal_precision)


def main():
    gen_alg = GABinary(1_000, BinarySimpleMutation(), 0.05, BinaryUniformCrossover(), 10_000, 4)

    func = FirstFunction()

    func_min = gen_alg.find_function_min(lambda x, y: 100 * (y - x**2)**2 + (1 - x)**2, 2, -4, 9)
    print(func_min)


if __name__ == '__main__':
    main()

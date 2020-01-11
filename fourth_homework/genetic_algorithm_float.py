from fourth_homework.genetic_algorithm import GA
from fourth_homework.crossovers.crossover import FloatAveragingCrossover
from fourth_homework.populations import FloatPopulation
from fourth_homework.functions.first_function import FirstFunction
from fourth_homework.mutations.mutations import FloatMutationLocalShift


class GAFloat(GA):
    def __init__(self,
                 population_size,
                 mutation,
                 mutation_prob,
                 crossover,
                 max_evaluations):
        super().__init__(population_size,
                         mutation,
                         mutation_prob,
                         crossover,
                         max_evaluations)

    def create_population(self, lower_limit, upper_limit, nr_of_variables):
        return FloatPopulation(lower_limit, upper_limit, nr_of_variables, self.population_size)


def main():
    gen_alg = GAFloat(1_000, FloatMutationLocalShift(), 0.05, FloatAveragingCrossover(), 10_000)

    func = FirstFunction()

    func_min = gen_alg.find_function_min(func, 2, -4, 9)
    print(func_min)


if __name__ == '__main__':
    main()

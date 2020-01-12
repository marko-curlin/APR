from statistics import median

from prettytable import PrettyTable

from fourth_homework.functions.function_factory import function_factory
from fourth_homework.genetic_algorithm_binary import GABinary
from fourth_homework.genetic_algorithm_float import GAFloat
from fourth_homework.mutations.mutations import FloatMutationLocalShift, BinarySimpleMutation
from fourth_homework.crossovers.crossover import FloatAveragingCrossover, BinaryUniformCrossover

LOWER_LIMIT = -50
UPPER_LIMIT = 150


# TODO: implement print in GA
def main():
    # print_headers('FIRST TASK', '#'*70)
    # first_task_float()
    # first_task_binary()
    # print_headers('SECOND TASK', '#'*70)
    # second_task_float()
    # second_task_binary()
    # print_headers('THIRD TASK', '#'*70)
    # third_task()
    # print_headers('FOURTH TASK', '#'*70)
    # fourth_task()
    print_headers('FIFTH TASK', '#'*70)
    fifth_task()



def first_task_float():
    float_GA = GAFloat(300, FloatMutationLocalShift(100_000), 0.05, FloatAveragingCrossover(), 1_000_000)

    func_nr_of_vars = {1: 2, 3: 5, 6: 2, 7: 2}

    for i in (1, 3, 6, 7,):
        print_headers('{}. FUNCTION - float'.format(i), '-' * 50)

        func = function_factory(i)
        min_value = 1
        while min_value > 1e-6:
            min_point = float_GA.find_function_min(func, func_nr_of_vars[i], LOWER_LIMIT, UPPER_LIMIT)
            min_value = func(*min_point)

        print('Min value: {} in point: {}'.format(min_value, min_point))


def first_task_binary():
    binary_GA = GABinary(900, BinarySimpleMutation(), 0.05, BinaryUniformCrossover(), 1_000_000, 3)

    func_nr_of_vars = {1: 2, 3: 5, 6: 2, 7: 2}

    for i in (1, 3, 6, 7,):
        print_headers('{}. FUNCTION - binary'.format(i), '-' * 50)

        func = function_factory(i)
        min_value = 1
        while min_value > 1e-4:
            min_point = binary_GA.find_function_min(func, func_nr_of_vars[i], LOWER_LIMIT, UPPER_LIMIT)
            min_value = func(*min_point)

        print('Min value: {} in point: {}'.format(min_value, min_point))


def second_task(gen_alg):
    for dim in (1, 3, 6, 10,):
        print_headers('DIMENSION: {}'.format(dim), '*' * 60)

        print_headers('6. FUNCTION - float', '-' * 50)

        func = function_factory(6)

        min_point = gen_alg.find_function_min(func, dim, LOWER_LIMIT, UPPER_LIMIT)
        min_value = func(*min_point)
        print('Min value: {} in point: {}'.format(min_value, min_point))

        print_headers('7. FUNCTION - float', '-' * 50)

        func = function_factory(7)

        min_point = gen_alg.find_function_min(func, dim, LOWER_LIMIT, UPPER_LIMIT)
        min_value = func(*min_point)
        print('Min value: {} in point: {}'.format(min_value, min_point))


def second_task_float():
    second_task(GAFloat(300, FloatMutationLocalShift(100_000), 0.05, FloatAveragingCrossover(), 1_000_000))


def second_task_binary():
    second_task(GABinary(900, BinarySimpleMutation(), 0.05, BinaryUniformCrossover(), 1_000_000, 3))


def get_results_for_third_task(GA, function, dimension, nr_of_executions):
    results = []
    for _ in range(nr_of_executions):
        min_point = GA.find_function_min(function, dimension, LOWER_LIMIT, UPPER_LIMIT)
        min_value = function(*min_point)
        results.append(min_value)

    return results


def get_table_row_for_third_task(GA, function_nr, dimension, nr_of_executions):
    results = get_results_for_third_task(GA, function_factory(function_nr), dimension, nr_of_executions)
    nr_of_hits = sum(map(lambda result: result < 1e-6, results))
    data_median = median(results)
    return str(type(GA)), dimension, function_nr, nr_of_hits, data_median


def third_task():
    table = PrettyTable(['GA', 'dimension', 'function', 'nr_of_hits', 'median value'])

    binary_GA = GABinary(500, BinarySimpleMutation(), 0.05, BinaryUniformCrossover(), 1e5, 4)
    float_GA = GAFloat(500, FloatMutationLocalShift(10_000), 0.05, FloatAveragingCrossover, 1e5)

    for dim in (3, 6):
        for i in (6, 7):
            table.add_row(get_table_row_for_third_task(float_GA, i, dim, 10))
            table.add_row(get_table_row_for_third_task(binary_GA, i, dim, 10))

    print(table)


def get_optimal_population_size(possible_population_sizes):
    result_medians = []
    for population_size in possible_population_sizes:
        float_GA = GAFloat(population_size, FloatMutationLocalShift(10_000), 0.05, FloatAveragingCrossover, 1e5)
        result_for_prob = []
        for _ in range(10):
            result_for_prob.append(float_GA.find_function_min(function_factory(6), 1, LOWER_LIMIT, UPPER_LIMIT)[0])
        result_medians.append(median(result_for_prob))
    return min(result_medians)


def get_optimal_mutation_prob(population_size, possible_mutation_probs):
    result_medians = []
    for mutation_prob in possible_mutation_probs:
        float_GA = GAFloat(population_size, FloatMutationLocalShift(10_000), mutation_prob, FloatAveragingCrossover, 1e5)
        result_for_prob = []
        for _ in range(10):
            result_for_prob.append(float_GA.find_function_min(function_factory(6), 1, LOWER_LIMIT, UPPER_LIMIT)[0])
        result_medians.append(median(result_for_prob))
    return min(result_medians)


def fourth_task():
    optimal_population_size = get_optimal_population_size((30, 50, 100, 200))
    optimal_mutation_prob = get_optimal_mutation_prob(optimal_population_size, (0.005, 0.01, 0.05, 0.1, 0.3))

    table = PrettyTable(('optimal_population_size', 'optimal_mutation_prob'))
    table.add_row((optimal_population_size, optimal_mutation_prob))
    print(table)


def fifth_task():
    func = function_factory(7)
    table = PrettyTable(('tournament_size', 'median_value'))
    for tournament_size in range(3, 8):
        float_GA = GAFloat(500, FloatMutationLocalShift(10_000), 0.05, FloatAveragingCrossover(), 1_000, tournament_size)
        result = []
        for _ in range(10):
            result.append(float_GA.find_function_min(func, 1, LOWER_LIMIT, UPPER_LIMIT)[0])
        table.add_row((tournament_size, median(result)))

    print(table)


def print_headers(title, marker):
    print("{} {} {}".format(marker, title, marker))


if __name__ == '__main__':
    main()

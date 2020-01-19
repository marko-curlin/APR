from math import cos, sin
import matplotlib.pyplot as plt

from fifth_homework.algorithms.direct_euler_method import DirectEulerMethod
from fifth_homework.algorithms.reverse_euler_method import ReverseEulerMethod
from fifth_homework.algorithms.trapezium_method import TrapeziumMethod
from fifth_homework.algorithms.runge_kutta_method import RungeKuttaMethod
from fifth_homework.algorithms.predictor_corrector_method import PredictorCorrectorMethod

from fifth_homework.utils.utils import frange

ALL_METHODS = ['direct_euler_method', 'reverse_euler_method', 'trapezium_method', 'runge_kutta_method',
               'predictor(direct_euler)_corrector(reverse_euler)_method',
               'predictor(direct_euler)_corrector(trapezium)_method']
all_results = []


def main():
    print_headers('FIRST TASK', '#'*70)
    first_task()
    print_headers('SECOND TASK', '#'*70)
    second_task()
    print_headers('THIRD TASK', '#'*70)
    third_task()
    print_headers('FOURTH TASK', '#'*70)
    fourth_task()


def first_task():
    A = [[0, 1], [-1, 0]]
    x_0 = [1, 1]
    T = 0.01
    t_max = 10

    args = (T, t_max, A, x_0)

    correct_result = [[x_0[0] * cos(t) + x_0[1] * sin(t), x_0[1] * cos(t) - x_0[0] * sin(t)] for t in frange(0, t_max, T)]

    print_results_for_first_task(DirectEulerMethod, args, correct_result)
    print_results_for_first_task(ReverseEulerMethod, args, correct_result)
    print_results_for_first_task(TrapeziumMethod, args, correct_result)
    print_results_for_first_task(RungeKuttaMethod, args, correct_result)

    args = (DirectEulerMethod, ReverseEulerMethod, T, t_max, 2, A, x_0)
    print_results_for_first_task(PredictorCorrectorMethod, args, correct_result)

    args = (DirectEulerMethod, TrapeziumMethod, T, t_max, 1, A, x_0)
    print_results_for_first_task(PredictorCorrectorMethod, args, correct_result)


def print_results_for_first_task(method_class, args, correct_result):
    print_headers(str(method_class).split('.')[-1][:-2], '-'*70)

    method = method_class(*args)
    result = method.solve_equation()

    if len(result) != len(correct_result):
        raise ValueError('Results must have the same lengths!')

    _sum = 0
    for i in range(len(correct_result)):
        _sum += abs(correct_result[i][0] - result[i][0]) + abs(correct_result[i][1] - result[i][1])

    print('{} error: {}'.format(str(method_class).split('.')[-1][:-2], _sum))

    if method_class != PredictorCorrectorMethod:
        all_results.append((result, list(frange(0, args[1], args[0]))))
    else:
        all_results.append((result, list(frange(0, args[3], args[2]))))


def second_task():
    A = [[0, 1], [-200, -102]]
    x_0 = [1, -2]
    T = 0.1
    t_max = 1

    args = (T, t_max, A, x_0)
    kwargs = {'print_after_iteration': 1}

    print_for_all_methods(args, kwargs)


def third_task():
    A = [[0, -2], [1, -3]]
    B = [[2, 0], [0, 3]]
    x_0 = [1, 3]
    r = [lambda t: 1, lambda t: 1]
    T = 0.01
    t_max = 10

    args = (T, t_max, A, x_0, B, r)
    kwargs = {'print_after_iteration': 100}

    print_for_all_methods(args, kwargs)


def fourth_task():
    A = [[1, -5], [1, -7]]
    B = [[5, 0], [0, 3]]
    x_0 = [-1, 3]
    r = [lambda t: t] * 2
    T = 0.01
    t_max = 1

    args = (T, t_max, A, x_0, B, r)
    kwargs = {'print_after_iteration': 10}

    print_for_all_methods(args, kwargs)


def print_for_all_methods(args, kwargs):
    print_results(DirectEulerMethod, args, kwargs)
    print_results(ReverseEulerMethod, args, kwargs)
    print_results(TrapeziumMethod, args, kwargs)
    print_results(RungeKuttaMethod, args, kwargs)

    temp_args = list(args)
    temp_args.insert(2, 2)
    args = [DirectEulerMethod, ReverseEulerMethod]
    args.extend(temp_args)
    print_results(PredictorCorrectorMethod, args, kwargs)

    args[1] = TrapeziumMethod
    args[4] = 1
    print_results(PredictorCorrectorMethod, args, kwargs)


def print_results(method_class, args, kwargs):
    print_headers(str(method_class).split('.')[-1][:-2], '-'*70)

    method = method_class(*args, **kwargs)
    result = method.solve_equation()

    if method_class != PredictorCorrectorMethod:
        all_results.append((result, list(frange(0, args[1], args[0]))))
    else:
        all_results.append((result, list(frange(0, args[3], args[2]))))


def print_headers(title, marker):
    print("{} {} {}".format(marker, title, marker))


def create_graphs():
    results = list(reversed(all_results))
    for task in range(1, 5):
        for method in ALL_METHODS:
            result = results.pop()
            x = result[1]
            y1 = list(map(lambda y: y[0], result[0]))
            y2 = list(map(lambda y: y[1], result[0]))

            plt.plot(x, y1, label='x1')
            plt.plot(x, y2, label='x2')

            plt.legend()
            plt.savefig('graph_images/task{}-{}.png'.format(str(task), method))
            plt.clf()



if __name__ == '__main__':
    main()
    create_graphs()

import dataclasses
from typing import List


@dataclasses.dataclass
class FloatUnit:
    point: List[float]
    value: int = None

    @property
    def dimension(self):
        return len(self.point)

    def evaluate_unit(self, fitness_function):
        self.value = fitness_function(*self.point)


class BinaryUnit:

    def __init__(self, point: List[List[int]], lower_limit, upper_limit):
        self.point = point
        self.real_point = self.calculate_real_point()
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit
        self.value = None

    @property
    def dimension(self):
        return len(self.point)

    @property
    def nr_of_bits(self):
        return len(self.point[0])

    def evaluate_unit(self, fitness_function):
        self.value = fitness_function(self.real_point)

    def calculate_real_point(self):
        point_int = []
        for binary_coordinate in self.point:
            point_int.append(int(''.join(binary_coordinate), 2))

        real_point = []
        for coordinate_int in point_int:
            real_coordinate = self.lower_limit + (self.upper_limit - self.lower_limit) * (coordinate_int / (2 ** self.nr_of_bits - 1))
            real_point.append(real_coordinate)

        return real_point

    @property
    def point(self):
        return self.point

    @point.setter
    def point(self, value: List[List[int]]):
        self.point = value
        self.real_point = self.calculate_real_point()

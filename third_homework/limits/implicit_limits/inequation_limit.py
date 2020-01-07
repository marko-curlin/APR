from typing import List

from third_homework.limits.implicit_limits.implicit_limit import ImplicitLimit

EPSILON = 10e-6


class InequationLimit(ImplicitLimit):

    def check_is_point_within_limit(self, point: List) -> bool:
        return self.func(*point) < 0

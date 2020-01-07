from typing import List

from third_homework.limits.explicit_limits.explicit_limit import ExplicitLimit


class LowerLimit(ExplicitLimit):

    def is_point_within_limit(self, point: List) -> bool:
        for limit_i, coordinate_i in zip(self.limit_value, point):
            if coordinate_i < limit_i:
                return False

        return True

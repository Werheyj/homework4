import math


def divide(first, second):
    if second == 0:
        return math.inf
    res = first/second
    return res


# divide(69, 0)

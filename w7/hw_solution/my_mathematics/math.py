import math


class MyMath:
    @staticmethod
    def sin(x: float) -> float:
        return math.sin(x)


class MyComplexMath:
    @staticmethod
    def sqrt(x):
        if x < 0:
            return (-x)**0.5 * 1.j
        else:
            return x**0.5


import math


def calculate_circle_area(radius: int | float) -> float:
    circle_area = math.pi * radius ** 2

    return circle_area


print(calculate_circle_area(2.5))

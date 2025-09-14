import math


class Shape:
    def calculate_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2


rectangle = Rectangle(4, 5)
circle = Circle(3)

print(f"Area of Rectangle: {rectangle.calculate_area()}")
print(f"Area of Circle: {circle.calculate_area()}")

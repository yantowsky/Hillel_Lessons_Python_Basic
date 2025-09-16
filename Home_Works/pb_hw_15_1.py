class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.get_square() == other.get_square()

    def __add__(self, other):
        square_new_rect = self.get_square() + other.get_square()
        return self.__class__(self.width, square_new_rect / self.width)

    def __mul__(self, n):
        square_new_rect = self.get_square() * n
        return self.__class__(self.width, square_new_rect / self.width)

    def __truediv__(self, n):
        square_new_rect = self.get_square() / n
        return self.__class__(self.width, square_new_rect / self.width)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'

r5 = r2 / 3
assert r5.get_square() == 6, 'Test5'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test6'
print('All tests passed')

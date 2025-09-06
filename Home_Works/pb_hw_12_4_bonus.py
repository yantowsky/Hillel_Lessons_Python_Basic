class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

# Перевірка:
rect = Rectangle(5, 10)
assert rect.calculate_area() == 50
print('OK')
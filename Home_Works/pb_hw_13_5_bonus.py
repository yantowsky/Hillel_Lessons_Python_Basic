def calculate_square_area(side):
    try:
        assert side > 0, "Side must be a positive number"
        return side ** 2
    except AssertionError as e:
        return e


# Перевірка:
area = calculate_square_area(4)  # Очікуваний результат: 16
print(area)

area = calculate_square_area(-3)  # Очікуваний результат: AssertionError: Side must be a positive number
print(area)

def check_positive(value):
    if value <= 0:
        raise ValueError('Value must be positive')


# Перевірка:
check_positive(5)  # Очікуваний результат: (без виводу, так як немає помилки)
try:
    check_positive(-3)  # Очікуваний результат: ValueError: Value must be positive
except ValueError as e:
        print(e)
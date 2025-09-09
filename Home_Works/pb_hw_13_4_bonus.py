def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero"


# Перевірка:
result = safe_divide(10, 2)
print(result)  # Очікуваний результат: 5

result = safe_divide(8, 0)
print(result)  # Очікуваний результат: "Error: Division by zero"

assert safe_divide(15, 3) == 5
print('Tests OK')

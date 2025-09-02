def add_decorator(number):
    """
    Реалізує декоратор, який змінює поведінку функції, додаючи до результату функції число.

    :param number: Число для додавання.
    :return: Декоратор для додавання числа до результату функції.
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) + number

        return wrapper

    return decorator


@add_decorator(5)
def example_function(x):
    return x * 2


assert example_function(2) == 9, 'Test_1'
assert example_function(0) == 5, 'Test_2'
assert example_function(-5) == -5, 'Test_3'
assert example_function(3) == 11, 'Test_4'
print('OK')

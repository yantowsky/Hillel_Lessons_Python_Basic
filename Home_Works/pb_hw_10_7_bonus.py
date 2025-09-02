def repeat_decorator(repeat_count):
    """
    Реалізує декоратор, який повторює виклик функції задану кількість разів.

    :param repeat_count: Кількість повторень.
    :return: Декоратор для повторюваного виклику функції.
    """

    def decorator(func):
        count = 0

        def wrapper(*args, **kwargs):
            nonlocal count

            for _ in range(repeat_count):
                count += 1
                func(*args, **kwargs)

            print(f'Function {func.__name__} called {count} times')
            print('=' * 50)

            return count

        return wrapper

    return decorator


@repeat_decorator(3)
def test_function_1():
    print(f"test_function_1")


assert test_function_1() == 3, "Test_1 failed"


@repeat_decorator(0)
def test_function_2():
    print(f"test_function_2")


assert test_function_2() is None, "Test_2 failed"


@repeat_decorator(100)
def test_function_3():
    print(f"test_function_3")


assert test_function_3() == 100, "Test_3 failed"


@repeat_decorator(5)
def test_function_4(a, b):
    print(f"test_function_4. Your args: {a}, {b}")


assert test_function_4(1, 2) == 5, "Test_5 failed"
print('OK')

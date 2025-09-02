def closure_example(x):
    """
    Реалізує функцію, яка використовує замикання для збереження значення.

    :param x: Початкове значення.
    :return: Функція, яка використовує замикання для збереження значення x.
    """
    result = x

    def inner_function(y):
        nonlocal result
        result += y
        return result

    return inner_function


closure_instance = closure_example(5)

assert closure_instance(3) == 8, "Test_1"
print('OK')

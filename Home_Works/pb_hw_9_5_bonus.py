def factorial(num: int) -> int | str:
    """
    This function returns the factorial of a number.

    Args:
        num (int): The number to factorial.

    Returns:
        int: The factorial.
        str: 'RecursionError' if num < 0
    """

    factorial_num = num * factorial(num - 1) if num > 1 else 1

    return 'RecursionError' if num < 0 else factorial_num


assert factorial(5) == 120, 'Test1'
assert factorial(0) == 1, 'Test2'
assert factorial(1) == 1, 'Test3'
assert factorial(10) == 3628800, 'Test4'
assert factorial(-10) == 'RecursionError', 'Test5'
print('OK')

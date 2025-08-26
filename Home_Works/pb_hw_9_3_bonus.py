import operator


def calculator(num1: int | float, num2: int | float, operation: str) -> int | float | str:
    """
    This function calculates the result of a given operation

    Args:
        num1 (int | float | str): The first number
        num2 (int | float | str): The second number
        operation (str): The operation to perform (add, sub, mul, div, pow)

    Returns:
        int | float | str: The result of the operation
    """

    dict_calc = {
        'add': operator.add(num1, num2),
        'sub': operator.sub(num1, num2),
        'mul': operator.mul(num1, num2),
        'div': operator.truediv(num1, num2) if num2 != 0 else "Division by zero",
        'pow': operator.pow(num1, num2),
    }

    result = dict_calc[operation] if operation in dict_calc else 0

    return result


assert calculator(5, 3, 'add') == 8, 'Test1'
assert calculator(5, 0, 'div') == "Division by zero", 'Test2'
assert calculator(5, 0, 'vid') == 0, 'Test3'
print('OK')
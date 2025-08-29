def is_even(digit: int) -> bool:
    """
    This function checks if a number is even.

    Args:
    digit (int): The number to be checked.

    Returns:
    bool: True if the number is even, False otherwise.
    """

    return True if digit % 2 == 0 else False


assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
print('OK')

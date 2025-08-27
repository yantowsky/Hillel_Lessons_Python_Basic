def square_numbers(numbers: list[int]) -> list[int]:
    """
    This function returns the square of the numbers

    Args:
    numbers (list[int]): a list of numbers

    Returns:
    list[int]: the square of the numbers
    """
    result = list(map(lambda x: x * x, numbers))

    return result


assert square_numbers([1, 2, 3, 4, 5]) == [1, 4, 9, 16, 25]
assert square_numbers([0, -1, -2, -3]) == [0, 1, 4, 9]
assert square_numbers([]) == []
assert square_numbers([3]) == [9]
assert square_numbers([1, 2, 3, 4, 5] * 250) == [1, 4, 9, 16, 25] * 250
print('OK')

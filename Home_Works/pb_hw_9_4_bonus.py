def multiply_even_numbers(numbers: list[int]) -> list[int]:
    """
    This function is used to multiply the even numbers by two.

    Args:
        numbers (list[int]): List of numbers to multiply.

    Returns: list[int]: List of numbers multiplied by two.
    """

    result = list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, numbers)))

    return result


assert multiply_even_numbers([1, 2, 3, 4, 5, 6]) == [4, 8, 12]
assert multiply_even_numbers([2, 4, 6, 8, 10, 12]) == [4, 8, 12, 16, 20, 24]
assert multiply_even_numbers([1, 3, 5, 7, 9, 11]) == []
assert multiply_even_numbers([]) == []
assert multiply_even_numbers([6]) == [12]
assert multiply_even_numbers([2, 4, 6, 8, 10, 12] * 333) == ([4, 8, 12, 16, 20, 24] * 333)
print('OK')

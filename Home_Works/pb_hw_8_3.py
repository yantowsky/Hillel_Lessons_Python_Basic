def find_unique_value(some_list: list) -> int | None:
    """
    This function finds the first unique value in the given list.

    Args:
        some_list (list): A list to find the first unique value in.

    Returns:
        int: The first unique value in the given list.
        None: The list is empty.
    """

    unique_num_list = [
        num
        for num in some_list
        if some_list.count(num) == 1
    ]

    return unique_num_list[0] if unique_num_list else None


assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
assert find_unique_value([3, 4, 5, 6]) == 3, 'Test4'
assert find_unique_value([3, 3, 3]) is None, 'Test5'
print("ОК")

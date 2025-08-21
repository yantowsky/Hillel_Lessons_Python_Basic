def add_one(some_list: list) -> list:
    some_list_to_num_plus_one = int(''.join(str(num) for num in some_list)) + 1
    num_to_mod_list_int = [int(item) for item in list(str(some_list_to_num_plus_one))]

    return num_to_mod_list_int


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")

def common_elements() -> set:
    list_num_multiple_three = [item for item in range(100) if item % 3 == 0]
    list_num_multiple_five = [item for item in range(100) if item % 5 == 0]

    my_intersection_set = set(list_num_multiple_three).intersection(set(list_num_multiple_five))

    return my_intersection_set


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print('OK')

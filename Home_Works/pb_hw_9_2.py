def difference(*args: int | float) -> int | float:
    diff_max_min_num = max(args) - min(args) if args else 0

    return round(diff_max_min_num, 2) if diff_max_min_num % 1 else diff_max_min_num


assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')

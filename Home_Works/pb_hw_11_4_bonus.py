def bubble_sort(arr):
    len_arr = len(arr)

    for step in range(len_arr - 1):
        for change in range(len_arr - 1 - step):
            if arr[change] > arr[change + 1]:
                arr[change], arr[change + 1] = arr[change + 1], arr[change]

    return arr


# Перевірка
assert bubble_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90], 'Test1'
assert bubble_sort([5, 2, 9, 1, 5, 6]) == [1, 2, 5, 5, 6, 9], 'Test2'
assert bubble_sort([3, 8, 1, 7, 2, 9, 6]) == [1, 2, 3, 6, 7, 8, 9], 'Test3'
print('OK')

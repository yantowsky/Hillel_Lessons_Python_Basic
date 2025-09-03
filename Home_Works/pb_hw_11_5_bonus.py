def binary_search(arr: list[int], target: int) -> int:
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + ((right - left) // 2)

        if arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            return mid

    return -1


# Перевірка
assert binary_search([11, 12, 22, 25, 34, 64, 90], 22) == 2
print('OK')

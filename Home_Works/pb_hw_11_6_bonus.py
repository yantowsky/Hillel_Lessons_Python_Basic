def linear_search(arr, target):
    for index, item in enumerate(arr):
        if item == target:
            return index
    return -1

# Перевірка
assert linear_search([64, 34, 25, 12, 22, 11, 90], 22) == 4, 'Test1'
print('OK')
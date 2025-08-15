user_number = int(input('Please enter your only positive integer: '))

list_numbers = list(str(user_number))

while len(list_numbers) > 1:
    result_add_numbers = 1

    for number in list_numbers:
        result_add_numbers *= int(number)

    list_numbers = list(str(result_add_numbers))

final_number = int(list_numbers[0])

print(f'{user_number} -> {final_number}')

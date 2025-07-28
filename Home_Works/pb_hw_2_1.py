four_digit_integer = int(input('Enter four digit integer: '))
print(four_digit_integer)

first_number = four_digit_integer // 1000
print(first_number)

second_number = four_digit_integer // 100 % 10
print(second_number)

third_number = four_digit_integer // 10 % 10
print(third_number)

fourth_number = four_digit_integer % 10
print(fourth_number)
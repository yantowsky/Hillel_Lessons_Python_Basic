five_digit_integer = int(input('Enter five digit integer: '))

first_number = five_digit_integer // 10000
second_number = five_digit_integer // 1000 % 10
third_number = five_digit_integer // 100 % 10
fourth_number = five_digit_integer // 10 % 10
five_number = five_digit_integer % 10

invert_number = (first_number + (second_number * 10) + (third_number * 10 ** 2) + (fourth_number * 10 ** 3) + (
        five_number * 10 ** 4))

print(f'Your number: {five_digit_integer} => Invert number: {invert_number}')

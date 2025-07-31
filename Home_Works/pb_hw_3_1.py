first_number = int(input('Enter first number: '))
second_number = int(input('Enter second number: '))
calculator_action = input('Enter calculator action (+ - * /): ')

result = 0
message = ''

if calculator_action == '+':
    result = first_number + second_number
elif calculator_action == '-':
    result = first_number - second_number
elif calculator_action == '*':
    result = first_number * second_number
elif calculator_action == '^':
    result = first_number ** second_number
elif calculator_action == '/' and second_number != 0:
    result = first_number / second_number
elif calculator_action == '/' and second_number == 0:
    message = f'Number {first_number} cannot be divided by zero'
else:
    message = 'You entered invalid calculator action'

if message:
    print(message)
else:
    print(f'{first_number} {calculator_action} {second_number} = {result}')

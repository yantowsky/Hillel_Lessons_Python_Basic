import random

my_list = [random.randint(1, 9) for i in range(random.randint(3, 10))]

mod_list = [my_list[0], my_list[2], my_list[-2]]

print(f'{my_list} == {mod_list}')
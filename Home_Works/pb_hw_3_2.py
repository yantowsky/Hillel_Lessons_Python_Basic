# my_list = [8, 12, 3, 4, 10]
# my_list = [12, 3, 4, 10]
# my_list = [1]
my_list = []

mod_list = my_list[-1:] + my_list[:-1]

print(f'{my_list} => {mod_list}')
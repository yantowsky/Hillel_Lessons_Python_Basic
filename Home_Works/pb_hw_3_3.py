# my_list = [1, 2, 3, 4, 5, 6]
# my_list = [1, 2, 3, 4, 5]
# my_list = [1, 2, 3]
# my_list = [1]
my_list = [0]

value_mid_odd_list = len(my_list) - (len(my_list) // 2)

mod_list = [my_list[:value_mid_odd_list], my_list[value_mid_odd_list:]]

print(f'{my_list} => {mod_list}')

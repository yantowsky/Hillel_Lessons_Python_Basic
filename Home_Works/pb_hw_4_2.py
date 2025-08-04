# my_list = [0, 1, 7, 2, 4, 8]
# my_list = [1, 3, 5]
# my_list = [6]
my_list = []

sum_elem_pair_ind = 0

for i,el in enumerate(my_list):
    if i % 2 == 0:
        sum_elem_pair_ind += el

result = sum_elem_pair_ind * my_list[-1] if my_list else 0

print(f'{my_list} => {result}')

# my_list =[0, 1, 0, 12, 3]
# my_list = [0]
# my_list = [1, 0, 13, 0, 0, 0, 5]
my_list =[9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

print(f'{my_list} -> ', end='')

for item in my_list:
    if item == 0:
        my_list.remove(item)
        my_list.insert(len(my_list), item)

print(my_list)
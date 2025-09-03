def is_even(number: int) -> bool:
    ##################  Option #1  ###################
    # list_last_digit_even = [0, 2, 4, 6, 8]
    #
    # last_digit_in_num = int(str(number)[-1])
    #
    # return last_digit_in_num in list_last_digit_even

    #################  Option #2  ####################
    return not number & 1


assert is_even(2494563894038 ** 2) == True, 'Test1'
assert is_even(1056897 ** 2) == False, 'Test2'
assert is_even(24945638940387 ** 3) == False, 'Test3'
print('OK')

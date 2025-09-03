def prime_generator(end):
    if end >= 2:
        yield 2

    for num in range(3, end + 1, 2):
        is_prime_num = True

        for i in range(3, round(num ** 0.5) + 1):
            if num % i == 0:
                is_prime_num = False
                break

        if is_prime_num:
            yield num


from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('OK')

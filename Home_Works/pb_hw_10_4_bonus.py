def counter(func):
    count = 0

    def wrapper(*args, **kwargs) -> int:
        nonlocal count
        count += 1

        func(*args, **kwargs)

        return count

    return wrapper


@counter
def example_function(*args, **kwargs):
    print("Inside the function")
    if args:
        print(f'Your args: {args}')
    if kwargs:
        print(f'Your kwargs: {kwargs}')
    print('=' * 50)


assert example_function() == 1, 'Test1 failed'

example_function()
example_function()

assert example_function() == 4, 'Test2 failed'

example_function(10, key1="value1", key2="value2")

assert example_function(key3="value3") == 6, 'Test3 failed'

print('TEST OK')

def counter(func):
    count = 0

    def wrapper(*args, **kwargs) -> int:
        nonlocal count
        count += 1

        print(f'Function {func.__name__} called {count} times: ', end='')

        func(*args, **kwargs)

        return count

    return wrapper


@counter
def example_function(your_name: str):
    print(f'Inside the function -> Hi, {your_name}!')


example_function('Eugene')
example_function('Tasia')
example_function('Andy')

assert example_function('Test1') == 4, 'Test1 failed'

example_function('Vika')
example_function('Igor')

assert example_function('Test2') == 7, 'Test2 failed'

print('TEST OK')

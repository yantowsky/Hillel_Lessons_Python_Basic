from typing import Callable, Any, Generator


def my_pow(x: int | float) -> int | float:
    return x ** 2


def some_gen(begin: int | float, end: int | float, func: Callable[[int | float], int | float]) -> Generator[
    int | float, None, None]:
    """
    This is a generator function

    Args:
    begin (int | float): The beginning of the range
    end (int | float): The end of the range
    func (function): The function to apply to each element

    Returns:
    Generator[int | float | None, None]: Generator function
    """

    for _ in range(end):
        yield begin
        begin = func(begin)


from inspect import isgenerator

gen = some_gen(2, 4, my_pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')

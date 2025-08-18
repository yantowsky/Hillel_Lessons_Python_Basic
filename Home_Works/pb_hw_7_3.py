import re


def second_index(text: str, some_str: str):
    list_index = []

    for match in re.finditer(some_str, text):
        list_index.append(match.start())

    return list_index[1] if len(list_index) > 1 else None


assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')

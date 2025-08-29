import re


def first_word(text: str) -> str:
    """
    This function returns the first word from the given text.

    Args:
    text (str): The text to find the first word from.

    Returns:
    str: The first word from the given text.
    """

    return re.search(r"[A-Za-z']+", text).group()


assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')

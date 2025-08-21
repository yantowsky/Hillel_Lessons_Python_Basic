import string


def is_palindrome(text: str) -> bool:
    mod_string = (
        ''.join(
            item
            for item in text
            if item not in string.punctuation
        )
        .lower()
        .replace(' ', '')
    )

    reversed_string = mod_string[::-1]

    return mod_string == reversed_string


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")

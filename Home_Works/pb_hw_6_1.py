import string

user_letters = input('Please enter two letters separated by a hyphen (Example: a-A): ')

start_letter, end_letter = user_letters.split('-')

index_start_letter = string.ascii_letters.index(start_letter)
index_end_letter = string.ascii_letters.index(end_letter)

mod_string_letters = ''

if index_start_letter > index_end_letter:
    mod_string_letters = string.ascii_letters[index_start_letter:] + string.ascii_letters[:index_end_letter + 1]
else:
    mod_string_letters = string.ascii_letters[index_start_letter:index_end_letter + 1]

print(f'"{user_letters}" -> {mod_string_letters}')

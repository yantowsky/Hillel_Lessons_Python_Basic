import string

# user_string = 'Python Community'
# user_string = 'i like python community!'
user_string = 'Should, I. subscribe? Yes!'

mod_string = ''.join(item for item in user_string if item not in string.punctuation).title().replace(' ', '')
hashtag_string = '#' + mod_string[:139]

print(f'{user_string} -> {hashtag_string}')

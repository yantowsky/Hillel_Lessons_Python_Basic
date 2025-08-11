import keyword

variable_name = input('Enter a variable name: ')

is_single_underscore = variable_name == '_'
is_identifier = variable_name.isidentifier()
is_lower = variable_name.islower()
is_not_keyword = variable_name not in keyword.kwlist

is_valid_variable = is_single_underscore or (is_lower and is_identifier and is_not_keyword)

print(is_valid_variable)
'''
reverse words of string without changing order
'''
# using list and in-built functions.

test_string = ' If the character does not exist, display an appropriate message. '

result_list = test_string.split()
result_string = ''

result_string += ' ' if test_string.startswith(' ') else ''

for word in result_list:
    result_string += ' ' + (word[::-1])

result_string += ' 'if test_string.endswith(' ') else ''

print(result_string)
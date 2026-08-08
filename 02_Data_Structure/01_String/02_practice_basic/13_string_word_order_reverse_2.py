'''
reverse words order of string
'''
# using list and in-built functions.


test_string = ' If the character does not exist, display an appropriate message. '

result_string = ''

result_list = test_string.split()

result_string += ' ' if test_string.endswith(' ') else ''

for word in result_list:
    result_string = word + ' ' + result_string


result_string += ' ' if test_string.startswith(' ') else ''

print(f"""
intial string : {test_string}
resul string : {result_string}
""")

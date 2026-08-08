'''
reverse order of word in string

Take a sentence and display in reverse word order

without using any inbuilt function

'''

test_string = 'Python is a powerful language'

result_string = sub_string = ''

for char in test_string:

    if ord(char) != 32:
        sub_string += char

    else:
        result_string = sub_string + result_string # adding substring in reverse order
        result_string = char + result_string # adding space

        sub_string = ''
        
result_string = sub_string + result_string

print(f"""
Initial string : {test_string}
result string : {result_string}
""")
'''
reverse each word without reversing order of words in string

Take a sentence  and display:

'''

test_string = 'Python is a powerful language'

sub_string = result_string = ''

for char in test_string:

    if ord(char) != 32:
        sub_string = char + sub_string

    else:
        result_string += sub_string # adding existing sub string
        result_string += char       # adding space
        sub_string = ''

result_string += sub_string

print(f"""
Initial string : {test_string}
Result string : {result_string}
""")
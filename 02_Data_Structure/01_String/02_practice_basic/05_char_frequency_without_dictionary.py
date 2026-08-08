'''
Character Frequency

Take a string as input and find the frequency of every character.

Ignore spaces and treat uppercase/lowercase letters as the same character

Not using dictionary
'''

test_case = 'Hello World'

checked = ''

for char in test_case:

    char = char.lower()
    char_count= 0

    if char not in checked and ord(char) != 32: # checking not visited and not a space
        for inner_char in test_case:
            inner_char = inner_char.lower() # not for case sensetive
            if inner_char == char:
                char_count += 1

        checked = checked + char
        print(f" Frequency of {char} : {char_count}")

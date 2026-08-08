'''
Character Frequency

Take a string as input and find the frequency of every character.

Ignore spaces and treat uppercase/lowercase letters as the same character

Using dictionary
'''

test_case = 'Hello World'

checked = {}

for char in test_case:

    if ord(char) != 32: # means if not a space
        char = char.lower() # not for case sensetive

        if char in checked :
            checked[char] += 1

        else:
            checked[char] = 1

print(f"Frequency of charectors is: {checked}")

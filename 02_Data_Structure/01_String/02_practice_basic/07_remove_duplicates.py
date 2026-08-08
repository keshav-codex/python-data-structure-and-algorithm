'''
Remove Duplicate Characters

Take a string and create a new string by removing duplicate characters while maintaining the original order.

Example:

Input: programming

Output: progamin

Do not use set() for the main solution.
'''


test_case = 'removing programming'

unique_string = ''

for char in test_case:

    char = char.lower()

    if char not in unique_string:
        unique_string += char

print(f" Unique string string is : {unique_string}")

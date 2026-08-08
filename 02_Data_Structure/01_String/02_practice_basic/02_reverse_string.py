'''
Reverse a String

Take a string  and reverse it.

Implement the program using a loop without using:

Slicing ([::-1])
reversed()
Any built-in function specifically designed to reverse a sequence
'''

test_string = "Implement the program using a loop without using Slicing and reversed()"
reverse_string = ''

for char in test_string:
    reverse_string = char + reverse_string

print(f"""
Original string is : {test_string}
Reversed strring is : {reverse_string}
""")
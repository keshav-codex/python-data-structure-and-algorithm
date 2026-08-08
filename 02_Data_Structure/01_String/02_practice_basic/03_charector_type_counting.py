'''
Character Type Counter

Take a string as input and count:

Uppercase letters
Lowercase letters
Digits
Spaces
Special characters

Do not use regular expressions.
'''

test_string = "TTTtttt11111      &*&%$#%"

total_char = count_upper = count_lower = count_digits = count_spaces = count_special = 0

for char in test_string:

    total_char +=1

    if char.isupper():
        count_upper += 1

    if char.islower():
        count_lower += 1

    if char.isdigit():
        count_digits += 1
    
    if char.isspace():
        count_spaces += 1

    if not char.isalnum() and not char.isspace():
        count_special += 1

print(f"""
    Total : {total_char}
    ********************
Uppercase : {count_upper}
Lowercase : {count_lower}
Digits    : {count_digits}
Spaces    : {count_spaces}
Special   : {count_special}

""")
    

    
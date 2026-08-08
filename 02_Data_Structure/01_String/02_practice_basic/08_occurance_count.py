'''
First and Last Occurrence

Take a character as input.

Find:

First occurrence of the character
Last occurrence of the character
Total number of occurrences

If the character does not exist, display an appropriate message.

Do not use find(), rfind(), or count() for the main logic.
'''
# Assuming for valid entry only one char and checking for case sensetive


test_string = 'Input a char from this string to check fist, last and total occurance : '

test_char = input(test_string)

if len(test_char) != 1:
    print("# Enter only one char # No blank # No more than one char")

else:

    first_occurance = last_occurance = total_occurance = position = 0

    for char in test_string:
        position += 1

        if char == test_char:
            if not first_occurance:
                first_occurance = position

            last_occurance = position
            total_occurance += 1

    if first_occurance:
    
        print(f"""
                charector : {test_char}
        first occurence position : {first_occurance}
        last occurence position : {last_occurance}
        total occurence position : {total_occurance}
        """)

    else:
        print(f"{test_char} is not in string")
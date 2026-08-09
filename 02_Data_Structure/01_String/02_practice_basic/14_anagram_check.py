# check string is anagram or not 
# not case sensetive
# trim spaces from both side

test_string = input("Enter a string to check is anagram or not : ")

if test_string == '':
    print("Empty string")

else:
    left = 0
    right = len(test_string) - 1
    anagram = True

    while left <= right:
        if (test_string[left].lower()) != (test_string[right].lower()):
            anagram = False
            break

        left += 1
        right -= 1

    print(f"{test_string} is an anagram") if anagram else print("Not an anagram")

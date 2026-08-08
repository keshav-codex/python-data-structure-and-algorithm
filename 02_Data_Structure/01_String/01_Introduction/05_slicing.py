'''
Character Position Finder
Given a string, print:

Use both positive and negative indexing.
'''

test_string='PYTHONPROGRAM'

#first char
print(test_string[0])

#last char
print(test_string[-1])

#third charector
print(test_string[2])

#third fromend
print(test_string[-3])

# even postion charector
print(test_string[::2])

#odd possition charector
print(test_string[1::2])

#First 3 characters
print(test_string[:3])

#Last 3 characters
print(test_string[-3::])

#Everything except the first character
print(test_string[2:])

#Everything except the last character
print(test_string[:-2:])

#Extract Middle Portion
start= len(test_string)//4
end= start + len(test_string)//2

print("Half is : ",test_string[start:end])

#Remove 2 Characters From Both Ends
print("Removed 2 char from both ends", test_string[2:-2])

#Every second character
print(test_string[2::2])

#Every third character
print(test_string[3::3])

#Every second character starting from index 1
print(test_string[1::2])

#Reverse a String Using Slicing
print(test_string[::-1])

#divide it into two parts and reverse each part individually using slicing.
check_string ='RatCat'

half= len(check_string)//2

first_part= check_string[:half:]
second_part= check_string[half:]

print(f"After raversing each part : {first_part[::-1] + second_part[::-1]}")

#Reverse using every second character
print("Reverse using every second character : ", test_string[::-2])
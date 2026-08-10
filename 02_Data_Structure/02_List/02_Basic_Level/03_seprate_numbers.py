'''
Separate Positive, Negative and Zero
Given a list of integers, create three separate lists:

Positive Negative Zero

Example:

Input:
[10, -5, 0, 8, -2, 0, 15]
Positive: [10, 8, 15]
Negative: [-5, -2]
Zero: [0, 0]
'''

test_string = [10, -5, 0, 8, -2, 0, 15]

positive_list = []
zero_list = []
neagative_list = []

for num in test_string:
    if num > 0:
        positive_list.append(num)
    elif num == 0:
        zero_list.append(num)
    else:
        neagative_list.append(num)
        
print("possitive list : ", positive_list)
print("zero list : ", zero_list)
print("neagtive list : ", neagative_list)


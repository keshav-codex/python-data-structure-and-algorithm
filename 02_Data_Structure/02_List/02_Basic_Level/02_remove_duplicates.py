'''
Remove Duplicate Elements

Given a list, create a new list containing only unique elements while preserving their original order.

Example:

Input:                                  Output:
[10, 20, 10, 30, 20, 40, 30]            [10, 20, 30, 40]

Do not use set().
'''

test_list = [10, 8, 20, 10,11,12, 30,8,7,13,30, 20, 40, 30]
result_list = []


for num in test_list:
    if num not in result_list:
        result_list.append(num)

print(result_list)

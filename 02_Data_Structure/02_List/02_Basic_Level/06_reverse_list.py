'''
Reverse a List Without Built-in Reverse

Given a list, create its reverse using a loop.
Do not use:

reverse()   reversed()  Slicing [::-1]

Example:
Input:
[10, 20, 30, 40, 50]
Output:
[50, 40, 30, 20, 10]
'''

test_list = [10, 20, 30, 40, 50]

l, r = 0, (len(test_list)-1)

while(l < r):
    test_list[l], test_list[r] = test_list[r], test_list[l]
    l += 1
    r -= 1

print("Result : ", test_list)
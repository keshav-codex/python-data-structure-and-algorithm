'''
8. Move All Zeros to the End

Given a list containing integers and zeros, move all zeros to the end while maintaining the relative order of the non-zero elements.

Example:

Input:
[0, 5, 0, 3, 8, 0, 2]

Output:
[5, 3, 8, 2, 0, 0, 0]
'''

test_list = [0, 5, 0, 3, 8, 0, 2]

sift_index = len(test_list)-1
i = 0

while i < sift_index:
    if test_list[i] == 0:
        test_list[i], test_list[sift_index] = test_list[sift_index], test_list[i]
        sift_index -= 1

    else:
        i += 1

print("result : ", test_list)
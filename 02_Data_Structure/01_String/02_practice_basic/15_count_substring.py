# count substring

'''
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.

Input Format

The first line of input contains the original string. The next line contains the substring.

Constraints


Each character in the string is an ascii character.

Output Format

Output the integer number indicating the total number of occurrences of the substring in the original string.

Sample Input

ABCDCDC
CDC
Sample Output

2
'''


def count_substring(string, sub_string):
    count =0
    check_index = 0
    for i in range(0, len(string)):
        if string[i] ==  sub_string[0]:
            check_index = i
            found = True
            for char in sub_string:
                if  check_index < len(string) and char == string[check_index]:
                    check_index += 1
                else:
                    found = False
            if found:
                count += 1
    return count

if __name__ == '__main__':
    string = 'ABCDCDC'
    sub_string = 'CDC'
    
    count = count_substring(string, sub_string)
    print(count)
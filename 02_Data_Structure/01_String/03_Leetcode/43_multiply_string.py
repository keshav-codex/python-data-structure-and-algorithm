# Given two non-negative integers num1 and num2 represented as strings, 
# return the product of num1 and num2, also represented as a string.

# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.


class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        if num1 == "0" or num2 == "0":
            return "0"

        result = [0] * (len(num1) + len(num2))

        for i in range(len(num1)-1, -1, -1):
            for j in range(len(num2)-1 , -1, -1):

                digit1 = int(num1[i])
                digit2 = int(num2[j])

                product = digit1 * digit2

                position = i+j+1
                result[position] += product

                result[position-1] += result[position] // 10
                result[position] %= 10

        while result[0] == 0:
            result.pop(0)

        return ''.join(str(digit) for digit in result)
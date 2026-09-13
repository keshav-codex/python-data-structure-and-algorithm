'''
Given a positive integer n:

Replace the number by the sum of the squares of its digits.
Repeat the process.
If the number becomes 1, it is a happy number.
If the process enters a cycle that never reaches 1, it is not happy.

'''

class Solution:
    def isHappy(self, n: int) -> bool:
        n_set = set()
        while True:
            n_sum = 0

            while n > 0:
                digit = n % 10
                n_sum += digit ** 2
                n = n // 10

            if n_sum == 1:
                return True

            elif n_sum in n_set:
                return False

            n_set.add(n_sum)
            n = n_sum
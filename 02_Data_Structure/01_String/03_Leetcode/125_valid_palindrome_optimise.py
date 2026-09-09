# Given a string s, return true if it is a palindrome, or false otherwise.

# Constraints:
# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:

            # Skip non-alphanumeric characters from left
            while left < right and not s[left].isalnum():
                left += 1

            # Skip non-alphanumeric characters from right
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare characters
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
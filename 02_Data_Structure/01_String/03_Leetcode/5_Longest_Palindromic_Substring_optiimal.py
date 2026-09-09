# Given a string s, return the longest palindromic substring in s.

class Solution:
    def longestPalindrome(self, s: str) -> str:

        start = 0
        end = 0

        # Function to expand around a center
        def expand(left, right):

            # Keep expanding while the characters at left and right are equal
            while ( left >= 0 and right < len(s) and s[left] == s[right] ):
                left -= 1
                right += 1

            # left and right are now one position outside the actual palindrome
            return left + 1, right - 1

        # Try every character as a center
        for i in range(len(s)):

            # Odd-length palindrome
            left1, right1 = expand(i, i)

            # Even-length palindrome
            left2, right2 = expand(i, i + 1)

            # Check odd-length palindrome
            if right1 - left1 > end - start:
                start = left1
                end = right1

            # Check even-length palindrome
            if right2 - left2 > end - start:
                start = left2
                end = right2

        # Return the longest palindrome
        return s[start:end + 1]
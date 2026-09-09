# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0

        for char in s:
            while i < len(t):
                if t[i] == char:
                    i += 1
                    break
                i += 1
            else:
                return False

        return True
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Constraints:
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_count = {}

        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        for char in t:
            if char not in char_count:
                return False

            char_count[char] -= 1

        return all(value == 0 for value in char_count.values())
 
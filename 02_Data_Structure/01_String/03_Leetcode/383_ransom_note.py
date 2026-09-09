# Given two strings ransomNote and magazine, 
# return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        if len(ransomNote) > len(magazine):
            return False

        char_count = {}

        for char in magazine:
            char_count[char] = char_count.get(char,0) +1


        for char in ransomNote:
            if char not in char_count:
                return False

            char_count[char] -= 1

            if char_count[char] < 0:
                return False
        
        return True
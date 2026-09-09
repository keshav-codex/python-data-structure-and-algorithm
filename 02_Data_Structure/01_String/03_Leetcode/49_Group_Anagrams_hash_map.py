# Given an array of strings strs, group the anagrams together. 
# You can return the answer in any order.

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # HashMap:
        map = {}

        for word in strs:

            # Create a frequency list for 26 lowercase English letters'
            char_count = [0] * 26

            # Count every character in the current word
            for char in word:
                index = ord(char) - ord('a')
                char_count[index] += 1

            # Convert list to tuple so it can be used as a HashMap key
            key = tuple(char_count)

            # If this key does not exist, create an empty group
            if key not in map:
                map[key] = []

            # Add the current word to its anagram group
            map[key].append(word)

        # Return all the grouped anagrams
        return list(map.values())
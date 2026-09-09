# Given an array of strings strs, group the anagrams together. 
# You can return the answer in any order.

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = []
        group = []
        checked = set()

        for i in range(len(strs)):

            if i in checked:
                continue

            group.append(strs[i])
            checked.add(i)
            char_count = {}

            for char in strs[i]:
                char_count[char] = char_count.get(char, 0) + 1

            j = i + 1

            while j < len(strs):

                if (j not in checked) and (len(strs[j]) == len(strs[i])):

                    found = True
                    j_char_count = {}

                    for char in strs[j]:

                        if char not in char_count:
                            found = False
                            break

                        j_char_count[char] = j_char_count.get(char, 0) + 1

                    if char_count != j_char_count:
                        found = False

                    if found:
                        group.append(strs[j])
                        checked.add(j)

                j += 1

            result.append(group)
            group = []

        return result
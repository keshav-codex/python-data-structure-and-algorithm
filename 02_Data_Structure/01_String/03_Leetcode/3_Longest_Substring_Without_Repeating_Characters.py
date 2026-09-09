# Given a string s, find the length of the longest substring without duplicate characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count_freq={}
        temp_string=""
        char_count=0

        for i in range(len(s)):

            if s[i] in temp_string:
                count_freq[temp_string] = char_count

                while s[i] in temp_string:
                    temp_string = temp_string[1:]
                    char_count -= 1

            temp_string += s[i]
            char_count += 1

        if temp_string:
            count_freq[temp_string] = char_count

        return max(count_freq.values(), default=0)
# Given a string s, find all longest substrings without duplicate characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> None:
        count_freq = {}
        temp_string = ""
        char_count = 0

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

        max_length = max(count_freq.values(), default=0)

        print("Maximum Length:", max_length)
        print("Longest Substrings:")

        for substring, length in count_freq.items():
            if length == max_length:
                print(substring)



# Test
solution = Solution()

s = "abcabcbb"

solution.lengthOfLongestSubstring(s)
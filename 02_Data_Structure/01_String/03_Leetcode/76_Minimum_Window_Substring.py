# Given two strings s and t of lengths m and n respectively, 
# return the minimum window substring of s such that 
# every character in t (including duplicates) is included in the window. 
# If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        result = ""
        result_len = float("inf")

        if len(s) < len(t) or not s or not t:
            return result

        t_char_count = {}

        for char in t:
            t_char_count[char] = t_char_count.get(char, 0) + 1

        left = 0
        right = len(t) - 1

        temp_char_count = {}

        for k in range(right + 1):
            temp_char_count[s[k]] = temp_char_count.get(s[k], 0) + 1

        while right < len(s):

            while True:

                valid = True

                for key in t_char_count:
                    if temp_char_count.get(key, 0) < t_char_count[key]:
                        valid = False
                        break

                if not valid:
                    break

                window_length = right - left + 1

                if window_length < result_len:
                    result = s[left:right + 1]
                    result_len = window_length

                temp_char_count[s[left]] -= 1
                left += 1


            right += 1

            if right < len(s):
                temp_char_count[s[right]] = temp_char_count.get(s[right], 0) + 1
        return result
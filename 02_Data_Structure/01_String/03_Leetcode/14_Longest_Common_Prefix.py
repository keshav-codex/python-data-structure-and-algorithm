# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".


# Constraints:
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.


from ast import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        test_str = strs[0]
        result=""
        
        for i in range(len(test_str)):
            for j in range(1,len(strs)):
                if i >= len(strs[j]) or test_str[i] != strs[j][i]:
                    return result
            
            result += test_str[i]

        return result
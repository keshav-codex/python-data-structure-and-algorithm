# Given a string s, return the longest palindromic substring in s.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrom={}
        for i in range(len(s)):
            left=i
            right= len(s)-1

            while right >= left:
                if s[left]==s[right]:
                    is_palindrom=True
                    temp_right=right-1
                    temp_left=left+1
                    while temp_right >= temp_left:
                        if s[temp_left] != s[temp_right]:
                            is_palindrom = False
                            break

                        temp_left += 1
                        temp_right -= 1

                    if is_palindrom:
                        palindrom[s[left:right+1]]=len(s[left:right+1])

                right = right-1
        
        return max(palindrom,key=palindrom.get)
# Given two strings needle and haystack, 
# return the index of the first occurrence of needle in haystack, 
# or -1 if needle is not part of haystack.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if needle == "":
            return 0
        
        for h in range(len(haystack)):

            if haystack[h] == needle[0]:
                temp_h = h+1
                n= 1
                found = True

                while(temp_h<len(haystack) and n<len(needle)):
                    if haystack[temp_h] != needle[n]:
                        found = False
                        break
                    
                    temp_h += 1
                    n += 1

                if found and n == len(needle):
                    return h

        return -1
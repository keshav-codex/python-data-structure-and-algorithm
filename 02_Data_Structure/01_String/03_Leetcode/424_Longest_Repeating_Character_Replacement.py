# You are given a string s and an integer k. 
# You can choose any character of the string -
# change it to any other uppercase English character. 
# You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter.
# you can get after performing the above operations.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        char_count={}
        longest= 0
        i=j=0
        
        while j<len(s):
            char_count[s[j]]=char_count.get(s[j],0) + 1
            
            max_count=max(char_count.values())
            window_length = j - i + 1

            if max_count + k >= window_length:
                longest=max(longest,len(s[i:j+1]))

            else:
                char_count[s[i]] -= 1
                i+=1
            
            j+=1

        return longest
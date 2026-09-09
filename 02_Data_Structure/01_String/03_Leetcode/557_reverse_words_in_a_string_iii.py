#Given a string s, reverse the order of characters in each word within a sentence 
# while still preserving whitespace and initial word order.

class Solution:
    def reverseWords(self, s: str) -> str:

        temp_string = ""
        result= ""

        for char in s:
            if not char.isspace():
                temp_string = char+temp_string

            else:
                if temp_string:
                    result += temp_string
                    temp_string = ""

                result += char

        result += temp_string
        return result
# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

class Solution:
    def myAtoi(self, s: str) -> int:

        result=""
        digit_read = False
        is_negative = False

        for i in range(len(s)):

            if not digit_read and s[i].isspace():
                continue

            if not s[i].isdigit():
                if not digit_read:
                    if s[i]=="-":
                        is_negative = True
                        digit_read=True
                        continue

                    if s[i]=="+":
                        digit_read=True
                        continue

                break

            digit_read = True
            result += s[i]

        if result:
            number = 0

            for char in result:
                digit = ord(char) - ord("0")
                number = number * 10 + digit

            if is_negative:
                number = -number

            if number < -2147483648:
                return -2147483648

            if number > 2147483647:
                return 2147483647

            return number

        return 0
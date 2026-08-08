'''
Password Validation With Strength Level

Create a password validator that classifies the password as:

Weak
Medium
Strong

Consider:

Password length
Uppercase letters
Lowercase letters
Digits
Special characters

Example:

Input: Python

Output: Weak
Reason: Password is too short and has no digit or special character.
Input: Python123

Output: Medium
Input: Python@123

Output: Strong
'''



def password_validator(password):

    if not password:
        output = 'empty'
        return output

    else:
        has_min_length = len(password) >= 8
        has_lower = any(char.islower() for char in password)
        has_upper = any(char.isupper() for char in password)
        has_digit = any(char.isdigit() for char in password)
        has_special = any(not char.isalnum() for char in password)

        # all above work like

        #has_special = False
        #for char in password:
            #if not char.isalnum():
            #has_special = True
            #break


        if has_lower and  has_upper and has_min_length and has_digit and has_special:
            output='strong'
            return output

        elif has_lower and has_upper and has_min_length and (has_digit or has_special):

            output= 'medium'
            return output

        else:
            output= 'weak'
            return output




def show_message(output):

    match output:

        case 'empty':
            print(f"""
            output: {output}
            Error: Password is empty or only have whitespace.
            """)

        case 'strong':
            print(f"""
            output: {output}
            Password validating all credential.
            """)

        case 'medium':
            print(f"""
            output: {output}
            Password missing few essential credential.
            """)

        case 'weak':
            print(f"""
            output: {output}
            Alert: Password is very weak.
            """)

def main():
    
    password = input("Enter your password : ").strip()
    output = password_validator(password)
    show_message(output)


if __name__ == "__main__":
    main()
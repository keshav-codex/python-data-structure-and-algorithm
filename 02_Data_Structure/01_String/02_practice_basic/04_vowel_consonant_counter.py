'''
Vowel and Consonant Analyzer

Take a string and count the number of:

Vowels
Consonants

Ignore digits, spaces, and special characters.

'''
test_string = 'Python Programming 123!'
vowel_list = 'aeiouAEIOU'

vowel_count = consonant_count  = 0

for char in test_string:
    if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
        if char in vowel_list:
            vowel_count += 1
        else:
            consonant_count  += 1

print(f"""
No of vowels : {vowel_count}
No of consonats : {consonant_count }
""")
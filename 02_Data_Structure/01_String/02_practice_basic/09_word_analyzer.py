'''
Word Analyzer

Take a sentence  and display:

Total number of words
Longest word and length
Shortest word and length
Number of characters excluding spaces

'''

# asssuming only a sub string of one length
# if any exist this program will keep first longest or shortest word

test_string = 'Python is a powerful language'

sub_string = ''
longest_word = ''
shortest_word = ''
word_count = total_char = 0 
sub_string_length = longest_word_length = shortest_word_length = 0

for char in test_string:

    if not char.isspace():

        total_char += 1
        sub_string += char
        sub_string_length += 1

        print(char, " **** ", sub_string) # for showing process only

    elif sub_string:
        word_count +=1


        if longest_word_length < sub_string_length:
            longest_word = sub_string
            longest_word_length = sub_string_length

        if shortest_word:
            if shortest_word_length > sub_string_length:
                shortest_word = sub_string
                shortest_word_length = sub_string_length
        else:
            shortest_word = sub_string
            shortest_word_length = sub_string_length

        # just for showing process
        print(f"""
                **************
                substring = {sub_string}
                shortest = {shortest_word}
                longest = {longest_word}
        
                """)

        sub_string_length = 0
        sub_string = ''



print(f"""
        String word report
Total number of words : {word_count}
Longest word        : {longest_word}
Longest word length : {longest_word_length}
Shortest word       : {shortest_word}
Shortest word length :{shortest_word_length}
Total char ex- space : {total_char}

""")
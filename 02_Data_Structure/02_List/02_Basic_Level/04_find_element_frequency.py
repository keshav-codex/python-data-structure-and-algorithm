'''
Find Element Frequency

Take a list and an element from the user.

Find:

Whether the element exists
Number of occurrences
First index where it occurs
Last index where it occurs

Do not use count(), index(), or other methods that directly solve the problem.
'''

# assuming for a valid type input

test_list = [10, 8, 20, 10,11,12, 30,8,7,13,30, 20, 40, 30]

u_input = int(input("Enter a number to check it's occurance : "))

number_exist = False

for n in range(len(test_list)-1):
    if test_list[n] == u_input:
        if number_exist == False:
            number_exist = True
            count_occurs = 1
            first_index = n
            last_index = n

        else:
            count_occurs += 1
            last_index = n

if number_exist:
    print(f"""
    Number exist : {number_exist}
    Total occurance : {count_occurs}
    first_index : {first_index}
    last_index : {last_index}
    """)

else:
    print("Number does not exist")
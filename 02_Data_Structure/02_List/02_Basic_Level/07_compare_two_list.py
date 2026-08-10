'''
Compare Two Lists

Take two lists and determine:
1. Whether they are exactly equal (same size and same value at same index)
2. Whether they contain the same elements regardless of order
   (duplicates must match in count too)
'''

list_1 = [10, 10, 20]
list_2 = [10, 20, 20]


# ---- Check 1: are the lists exactly equal? ----
# same length AND same value at every matching index

same_len = len(list_1) == len(list_2)

exactly_equal = same_len  # start by assuming True only if lengths match

if same_len:
    # only safe to compare index by index if lengths match
    for i in range(len(list_1)):
        if list_1[i] != list_2[i]:
            exactly_equal = False
            break


# ---- Check 2: do they contain the same elements (duplicates counted)? ----
# for every number, its count in list_1 must match its count in list_2

same_elements = same_len  # different lengths can never have matching counts

if same_elements:
    for num in list_1:
        count_in_list_1 = list_1.count(num)
        count_in_list_2 = list_2.count(num)
        if count_in_list_1 != count_in_list_2:
            same_elements = False
            break


# ---- print results ----
print('Printing result')

if exactly_equal:
    print('Exactly same list')
else:
    print('Not same list')

if same_elements:
    print('Same elements (duplicates match)')
else:
    print('Not same elements')
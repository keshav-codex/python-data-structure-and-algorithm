'''
Find Common Elements

Given two lists, create a third list containing elements that occur in both lists.

Maintain the order in which elements appear in the first list.

Example:

List 1:                    List 2:                  Output:    
[10, 20, 30, 40, 50]        [30, 50, 60, 20]        [20, 30, 50]

Avoid using set() for the main solution.
'''

list_1 = [30, 50, 60, 20] 
list_2 = [10, 20, 30, 40, 50]
result = []

for num in list_2:
    if num in list_1 and num not in result:
        result.append(num)

print(f"Common element list : {result}")
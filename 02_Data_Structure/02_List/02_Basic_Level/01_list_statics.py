'''
1. List Statistics

Take a list of numbers and find:

Total number of elements
Sum of elements
Largest element
second largest
Smallest element
second smallest
Average
Even numbers
Odd numbers
Zeros

'''

Test_list = [12, 5, 0, 8, 7, 9, 0, 11, 12, 4]

element_count = total_sum = even_count = odd_count = zeros = 0
largest = second_largest = smallest = second_smallest = None

for num in Test_list:
    element_count += 1
    total_sum += num

    if num == 0:
        zeros += 1

    if num %2 == 0:
        even_count += 1

    elif num %2 == 1:
        even_count += 1

    if second_largest is None or  (num > second_largest and num != largest):
        if largest is None or num > largest:
            second_largest = largest
            largest = num
        else:
            second_largest = num

    if second_smallest is None or (num < second_smallest and num != smallest):
        if smallest is None or num < smallest:
           second_smallest = smallest
           smallest = num
        else:
           second_smallest = num


if element_count == 0:
    print("No element in list")

else:
    print(f"""
    List statics
    ***********
    total numbers : {element_count}
    sum of elements : {total_sum}
    average : {total_sum/element_count:.4f}
    zeros count : {zeros}
    even count : {even_count}
    odd count : {odd_count}
    largest is : {largest}
    second largest is : {second_largest}
    smallest is : {smallest}
    second smallest is : {second_smallest}
    """)
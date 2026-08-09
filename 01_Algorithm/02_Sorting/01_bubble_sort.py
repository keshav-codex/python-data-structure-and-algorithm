# Bubble sort
# Move Largest to end of right before previos larger element
# concept : Compare adjacent elements and swap them if they are in the wrong order.

# Complexity
# Case	Time
# Best*	O(n)
# Average	O(n²)
# Worst	O(n²)
# Space	O(1)

def bubble_sort(test_array):

    len_array = len(test_array)

    for i in range(len_array):

        swapped = False # for optimization
        
        for j in range(len_array - i -1):
            if test_array[j] > test_array[j+1]:
                test_array[j], test_array[j+1] = test_array[j+1], test_array[j]
                swapped = True

        if not swapped:
            break

    print(f"Sorted array : {test_array}")


def main():
    test_array = [10,20,45,65,42,81,41,62,35]
    bubble_sort(test_array)

if __name__ == "__main__":
    main()
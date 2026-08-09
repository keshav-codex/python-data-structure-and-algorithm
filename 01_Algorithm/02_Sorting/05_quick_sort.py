# quick sort
# uses devide and conqure
# it select a pivot and do partition around it.

# pivot can ba anything
# first element     last element        middle element      random element

# put pivot at it's correct position/index

# Complexity
# Case	Time
# Best	O(n log n)
# Average	O(n log n)
# Worst	O(n²)

# Space depends on implementation/recursion depth.


def quick_sort(test_array,low,high):
    if low<high:
        partition_index = partition(test_array,low,high)
        quick_sort(test_array,low,partition_index-1)
        quick_sort(test_array,partition_index+1,high)


def partition(test_array,low,high):
    pivot= test_array[low]
    i, j = low, high

    while i<j:
        while test_array[i] <= pivot and i < high:
            i += 1

        while test_array[j] > pivot and j > low:
            j -= 1

        if i < j:
            test_array[i], test_array[j] = test_array[j], test_array[i]

    test_array[j] , test_array[low] = test_array[low], test_array[j]
    

    return j



def main():
    
    test_array = [10,20,3,80, 30, 30,2, 45,3,65, 65,2 ,42,81,41,62,10,35]
    low,high = 0, len(test_array)-1
    quick_sort(test_array, low, high)
    print(f"result_array is : {test_array}")


if __name__ == "__main__":
    main()
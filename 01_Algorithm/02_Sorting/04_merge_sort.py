# merge sort

# Uses divide and conquer.
# Divides the array into smaller parts.
# Merges sorted parts.
# Guaranteed O(n log n).
# Requires additional memory for typical array implementation.
# Stable.

# Complexcity
# Best     → O(n log n)
# Average  → O(n log n)
# Worst    → O(n log n)
# Space    → O(n)

def merge_sort(test_array):

    if len(test_array) <= 1:
        return test_array

    mid = len(test_array)//2

    left_array = merge_sort(test_array[:mid])
    right_array = merge_sort(test_array[mid:])

    result_array = conquer(left_array,right_array)

    return result_array


def conquer(left_array,right_array):
    
    left_len , right_len = len(left_array), len(right_array)
    l = r = 0
    result_array = []

    while l < left_len and r < right_len:
        if left_array[l] <= right_array[r]:
            result_array.append(left_array[l])
            l += 1

        else:
            result_array.append(right_array[r])
            r += 1


    if l < left_len:
        while l < left_len:
            result_array.append(left_array[l])
            l += 1

    if r < right_len:
        while r < right_len:
            result_array.append(right_array[r])
            r += 1

    return result_array


def main():
    test_array = [10,20,80, 30, 30, 45,65, 65, 42,81,41,62,35]
    result_array = merge_sort(test_array)
    print(f"result_array is : {result_array}")

if __name__ == "__main__":
    main()
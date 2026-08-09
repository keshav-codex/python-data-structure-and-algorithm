# insertion sort

# concept : build a sorted portion incrementally
# like playing card
# very good for small and nearly sorted data

# Complexity
# Case	Time
# Best	O(n)
# Average	O(n²)
# Worst	O(n²)
# Space	O(1)

def insertion_sort(test_array):
    for j in range(1, len(test_array)):

        if test_array[j] < test_array[j-1]:
            check_value = test_array[j]

            while test_array[j-1] > check_value and j >= 1:
                test_array[j] = test_array[j-1]
                j -= 1

            test_array[j] = check_value 

    print(f"""
    sorted array is:
    {test_array}
    """)


def main():
    test_array = [10,20,45,65,42,81,41,62,35]
    insertion_sort(test_array)

if __name__ == "__main__":
    main()
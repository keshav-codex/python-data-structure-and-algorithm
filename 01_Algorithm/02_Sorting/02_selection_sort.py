# selsection sort

# motto : sorted data
# concept : find smallest element and palce it at right place
# again find smallest from remaining

# Complexity
# Case	Time
# Best	O(n²)
# Average	O(n²)
# Worst	O(n²)
# Space	O(1)

def selection_sort(test_array):
    for i in range(len(test_array)):
        min_value_index = i

        for j in range(i+1,len(test_array)):
            if test_array[j] < test_array[min_value_index]:
                min_value_index = j
                test_array[min_value_index], test_array[i] = test_array[i],test_array[min_value_index]

    print(f"""
    Array after sorting :
    {test_array}
    """)


def main():
    test_array = [10,20,45,65,42,81,41,62,35]
    selection_sort(test_array)

if __name__ == "__main__":
    main()
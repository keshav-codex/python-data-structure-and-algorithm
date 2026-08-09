# Linear search

numbers = [10, 25, 60, 50, 40, 30, 45, 50]
target = 30


for i in range(len(numbers)):
    if numbers[i] == target:
        print(f"{target} found at index {i}")
        break

else:
    print("Target not found")

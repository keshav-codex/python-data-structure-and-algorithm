# Binary search

numbers = [10, 25, 30, 40, 45, 50, 60,65 ,70, 80, 85, 90, 95]
target = 105

low = 0
high = len(numbers)-1

while low <= high:
    mid = low + (high - low )//2

    if numbers[mid] == target:
        print(f"{target} found at index {mid}")
        break

    elif numbers[mid] < target:
        low = mid + 1

    else:
        high = mid - 1

else:
    print(target, " not found")
"""
List Slicing
------------

Syntax:
    list[start:stop:step]

start -> included
stop  -> excluded
step  -> movement
"""

numbers = [10, 20, 30, 40, 50, 60]

# Positive indexing
print(numbers[0])          # 10
print(numbers[2])          # 30

# Negative indexing
print(numbers[-1])         # 60
print(numbers[-2])         # 50

# Basic slicing
print(numbers[1:4])        # [20, 30, 40]
print(numbers[:4])         # [10, 20, 30, 40]
print(numbers[2:])         # [30, 40, 50, 60]

# Step
print(numbers[::2])        # [10, 30, 50]
print(numbers[1::2])       # [20, 40, 60]

# Negative step
print(numbers[::-1])       # [60, 50, 40, 30, 20, 10]
print(numbers[4:1:-1])     # [50, 40, 30]

# Copy using slicing
copy_numbers = numbers[:]
print(copy_numbers)
print(copy_numbers is numbers)    # False

# Slicing does not modify the original list
part = numbers[1:4]

print(part)
print(numbers)

string_t = 'keshav@jha.com'

print((string_t.index('@')))
print((string_t.index('.')))
print(string_t[:string_t.index('@')])
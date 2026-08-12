"""
Set Creation and Basic Operations
"""

# Creation
numbers = {10, 20, 30}
print(numbers)

# Duplicate values are automatically removed
numbers = {10, 20, 10, 30, 20}
print(numbers)

# Empty set
empty_set = set()
print(empty_set)

# Different data types
data = {10, "Python", 3.14, True}
print(data)

# Assignment
numbers = {10, 20, 30}

# User input
numbers = set(map(int, input("Enter numbers: ").split()))
print(numbers)

# View
print(numbers)

# Add
numbers.add(40)
print(numbers)

# Add multiple elements
numbers.update([50, 60])
print(numbers)

# Remove
numbers.remove(20)
print(numbers)

# Safe remove
numbers.discard(100)
print(numbers)

# Membership
print(30 in numbers)

# Clear
numbers.clear()
print(numbers)
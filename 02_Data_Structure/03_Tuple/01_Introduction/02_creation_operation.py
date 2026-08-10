"""
Tuple Creation and Basic Operations
"""

# Creation
empty = ()
numbers = (10, 20, 30)
mixed = (10, "Python", True, 3.14)
print(numbers)
print(mixed)

# Without parentheses
numbers = 10, 20, 30
print(numbers)

# Assignment
numbers = (10, 20, 30)
a, b, c = numbers
print(a)
print(b)
print(c)

# User input
numbers = tuple(
    map(int, input("Enter numbers: ").split())
)
print(numbers)


# View / Access
print(numbers[0])
print(numbers[-1])

# Check membership
print(20 in numbers)

# Concatenation
a = (1, 2)
b = (3, 4)
c = a + b
print(c)

# Repetition
print((1, 2) * 3)

# Count and index
print(numbers.count(20))
print(numbers.index(20))

# Tuple cannot be modified
# numbers[0] = 100
# TypeError
"""
TUPLE
-----

- Ordered collection
- Immutable
- Allows duplicate values
- Supports different data types
- Supports indexing and slicing
- Zero-based indexing
- Usually written using ()
"""

numbers = (10, 20, 30, 20)

print(numbers)
print(type(numbers))


# Built-in functions

print(len(numbers))
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print(sorted(numbers))       # Returns a list
print(tuple([1, 2, 3]))


# Tuple methods

print(numbers.count(20))
print(numbers.index(30))
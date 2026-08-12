"""
SET
---

- Unordered collection
- Mutable
- Does not allow duplicate values
- Supports different data types
- No indexing or slicing
- Created using {}
"""

numbers = {10, 20, 30, 20}

print(numbers)          # {10, 20, 30}
print(type(numbers))


# Built-in functions

print(len(numbers))
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print(sorted(numbers))  # Returns a list


# Important set methods

numbers.add(40)
numbers.update([50, 60])

numbers.remove(20)
numbers.discard(30)

print(numbers)

print(numbers.pop())    # Removes an arbitrary element
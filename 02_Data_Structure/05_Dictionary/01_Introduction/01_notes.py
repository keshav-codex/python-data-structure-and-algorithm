
"""
Dictionary
----------

- Stores data as key-value pairs.
- Mutable.
- Ordered (Python 3.7+).
- Keys must be unique and hashable.
- Values can be of any data type.
- Supports adding, updating and deleting.
- Accessed using keys, not numeric indexes.
- Created using {} or dict().
"""

student = {
    "name": "Keshav",
    "age": 28,
    "marks": 85
}


# Built-in functions

print(len(student))
print(type(student))
print(bool(student))


# Dictionary methods

print(student.keys())          # All keys
print(student.values())        # All values
print(student.items())         # Key-value pairs

print(student.get("name"))     # Safe access
print(student.get("city", "Delhi"))

student.update({"age": 29, "city": "Delhi"})

print(student.pop("age"))      # Remove and return value
print(student.popitem())       # Remove last inserted pair

student.clear()
print(student)


# Membership checks keys

student = {"name": "Keshav", "age": 28}

print("name" in student)       # True
print("Keshav" in student)     # False

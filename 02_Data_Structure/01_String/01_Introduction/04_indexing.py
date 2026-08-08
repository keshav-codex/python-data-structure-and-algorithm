
"""
String Indexing
----------------
Indexing is used to access individual characters from a string.

Positive indexing:
    Starts from 0 → left to right

Negative indexing:
    Starts from -1 → right to left



# ---------------------------------------------------------
# 1. String
# ---------------------------------------------------------
"""
text = "Python"

# Characters:
#
# Positive Index:
#   P   y   t   h   o   n
#   0   1   2   3   4   5
#
# Negative Index:
#   P   y   t   h   o   n
#  -6  -5  -4  -3  -2  -1


# ---------------------------------------------------------
# 2. Positive Indexing
# ---------------------------------------------------------

print(text[0])     # P → first character
print(text[1])     # y
print(text[2])     # t
print(text[5])     # n


# ---------------------------------------------------------
# 3. Negative Indexing
# ---------------------------------------------------------

print(text[-1])    # n → last character
print(text[-2])    # o
print(text[-3])    # h
print(text[-6])    # P → first character


# ---------------------------------------------------------
# 4. Accessing Characters Using Variables
# ---------------------------------------------------------

index = 3

print(text[index])     # h


# ---------------------------------------------------------
# 5. Index Out of Range
# ---------------------------------------------------------

# print(text[6])
# IndexError: string index out of range

# Valid positive indexes: 0 to len(text) - 1
# Valid negative indexes: -1 to -len(text)


# ---------------------------------------------------------
# 6. Important Point
# ---------------------------------------------------------

# Strings are immutable.
# We can access a character using an index,
# but we cannot modify a character directly.

# text[0] = "J"
# TypeError: 'str' object does not support item assignment

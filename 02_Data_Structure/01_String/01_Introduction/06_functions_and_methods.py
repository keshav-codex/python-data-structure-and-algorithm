
"""
String Built-in Functions and Methods
"""

text = "  Python Programming  "


# ---------------------------------------------------------
# Built-in Functions
# ---------------------------------------------------------

print(len(text))              # Length of string
print(type(text))             # Data type
print(str(123))               # Convert value to string
print(list("Python"))         # Convert string to list
print(tuple("Python"))        # Convert string to tuple
print(sorted("python"))       # Returns sorted list


# ---------------------------------------------------------
# Case Methods
# ---------------------------------------------------------

print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())
print(text.swapcase())


# ---------------------------------------------------------
# Whitespace Methods
# ---------------------------------------------------------

print(text.strip())
print(text.lstrip())
print(text.rstrip())


# ---------------------------------------------------------
# Search Methods
# ---------------------------------------------------------

word = "Python Programming"

print(word.find("Python"))        # Position, -1 if not found
print(word.index("Python"))       # Position, ValueError if not found
print(word.count("m"))            # Number of occurrences
print(word.startswith("Python"))
print(word.endswith("ing"))


# ---------------------------------------------------------
# Modification Methods
# ---------------------------------------------------------

print(word.replace("Python", "Java"))


# ---------------------------------------------------------
# Split and Join
# ---------------------------------------------------------

data = "Python,Java,C++"

items = data.split(",")
print(items)

print("-".join(items))


# ---------------------------------------------------------
# Checking Methods
# ---------------------------------------------------------

print("Python".isalpha())
print("12345".isdigit())
print("Python123".isalnum())
print("   ".isspace())
print("python".islower())
print("PYTHON".isupper())


# ---------------------------------------------------------
# Useful Operations
# ---------------------------------------------------------

print("Python" in "Python Programming")
print("Java" not in "Python Programming")

"""
Dictionary Creation and Basic Operations
"""

# ---------------------------------------------------------
# Creation
# ---------------------------------------------------------

student = {
    "name" : "keshav",
    "age"  : 28,
    "city" : "Delhi"
}

print(student)

# Empty dictionary

data = {}
print(data)

data = dict()
print(data)

# ---------------------------------------------------------
# Assignment
# ---------------------------------------------------------

student["course"] = "pyhton"    #add
student["age"] = 24

print(student)

# ---------------------------------------------------------
# User Input
# ----------------------------------

name = input("Enter student name : ")
age = int(input("enter age : "))

student = {
    'name' : name,
    'age'  : age
}

print(student)

# ---------------------------------------------------------
# View / Access
# ---------------------------------------------------------

print(student["age"])
print(student.get("city"))  #None if key doesn't exist
print(student.get("city","delhi"))

# ---------------------------------------------------------
# Add / Update
# ---------------------------------------------------------

student["city"] = "Mumbai"
student.update({"age": 30, "course": "python"})
print(student)

# ---------------------------------------------------------
# View Keys, Values and Items
# ---------------------------------------------------------

print(student.keys())
print(student.values())
print(student.items())

# ---------------------------------------------------------
# Check Key
# ---------------------------------------------------------

print("name" in student)
print("salary" not in student)

# ---------------------------------------------------------
# Delete
# ---------------------------------------------------------

student.pop("age")
print(student)

student.popitem()                  # Removes last inserted pair
print(student)

# del

del student["name"]
print(student)

# Clear

student.clear()
print(student)
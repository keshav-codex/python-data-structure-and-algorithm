'''
Set Operations Analyzer

Given two sets of numbers:
set_a = {10, 20, 30, 40, 50}
set_b = {30, 40, 50, 60, 70}

Perform and display:
Union
Intersection
Difference of set_a from set_b
Difference of set_b from set_a
Symmetric difference
Check whether set_a and set_b have any common elements
Check whether set_a is a subset of set_b
Check whether set_a is a superset of set_b

Expected output:
Union: {10, 20, 30, 40, 50, 60, 70}
Intersection: {30, 40, 50}
A - B: {10, 20}
B - A: {60, 70}
Symmetric Difference: {10, 20, 60, 70}
Common Elements: Yes
A is subset of B: No
A is superset of B: No

Focus: This single problem gives practice with the major set operations and relationship
checks without introducing advanced concepts.

'''

set_a = {10, 20, 30, 40, 50}
set_b = {30, 40, 50, 60, 70}

print("Set Union")
print(set_a | set_b)

print("Set intersection")
print(set_a and set_b)

print("Difference of set_a from set_b")
print(set_a - set_b)

print("Difference of set_b from set_a")
print(set_b - set_a)

print("Symmetric Difference: {10, 20, 60, 70}")
print(set_a ^ set_b)

#Check whether set_a and set_b have any common elements
print("Have common element") if not set_a ^ set_b else print("Not have common element")

# Check whether set_a is a subset of set_b
print("A is subset of B") if set_a in set_b else print("A is not a subset of B")

# Check whether set_a is a superset of set_b
print("A is superset of B") if set-b in set_a else print("A is subset of B")
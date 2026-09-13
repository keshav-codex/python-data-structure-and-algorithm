# anylyse 2 given sets

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# Find the intersection of the two sets
intersection = set1 & set2

# Find the union of the two sets
union = set1 | set2

# Find the difference between the two sets
difference = set1 - set2

print("Intersection:", intersection)
print("Union:", union)
print("Difference:", difference)

# is set1 a subset of set2?
is_subset = set1.issubset(set2)
print("Is set1 a subset of set2?", is_subset)

# is set1 a superset of set2?
is_superset = set1.issuperset(set2)
print("Is set1 a superset of set2?", is_superset)

# Check if the two sets are disjoint (no common elements)
are_disjoint = set1.isdisjoint(set2)
print("Are the two sets disjoint?", are_disjoint)
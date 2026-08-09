"""
LIST
----

A list is an ordered, mutable collection of objects.

Key Points:
- Ordered
- Mutable
- Allows duplicate values
- Supports different data types
- Supports indexing and slicing
- Zero-based indexing
- Dynamic size
- Created using []
"""
# creating empty list
numbers = []
print(numbers)

# assigning direct value
numbers = [10, 20, 30, 40]
print(numbers)
print(type(numbers))

# direct creation and assignment
names = ["Keshav", "Rahul", "Amit"]
print(names)

#different data type
data = [10, "Python", 3.14, True]
print(data)


# assignment to update a possition
numbers[0] = 100
print(numbers) # [100, 20, 30]

# making list by list() function
numbers = list((10, 20, 30))
print(numbers)

#string to list
chars = list("Python")
print(chars) # ['P', 'y', 't', 'h', 'o', 'n']

test = 'Test string'
char_list = list(test)
print(char_list)


# range to list
numbers = list(range(1, 6))
print(numbers) # [1, 2, 3, 4, 5]

# built in functions
numbers = [10, 30, 20, 40, 50]

print(len(numbers))       # 5
print(type(numbers))      # <class 'list'>
print(min(numbers))       # 10
print(max(numbers))       # 50
print(sum(numbers))       # 150
print(sorted(numbers, reverse=True)) #Returns a new sorted list. does not modify original list

# imortent list methods
numbers = [10, 20, 30]

numbers.append(40) # append() → adds one element at the end.
print(numbers)

numbers.insert(1, 15) #insert() → adds at a specific index.
print(numbers)

numbers.extend([50, 60]) #extend() → adds multiple elements.
print(numbers)

numbers.remove(15) #remove() → removes by value.
print(numbers)

value = numbers.pop() #pop() → removes and returns by index; default is last.
print(value)

numbers.reverse()
print(numbers)

numbers.sort() #→ modifies the original list.
print(numbers) # sorted() → returns a new list.

print(numbers.count(20))
print(numbers.index(20))

numbers.clear()#clear() → removes all elements.
print(numbers)
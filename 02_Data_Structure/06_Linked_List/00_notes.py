"""
LINKED LIST
-----------

A linked list is a linear data structure made of nodes.

Each node contains:
    1. Data
    2. Reference to another node

Basic structure:

    [Data | Next] -> [Data | Next] -> [Data | None]


HEAD
----
- Head stores the reference to the first node.
- Empty linked list: head = None


NODE
----
A node is an object containing data and a link/reference.


TYPES
-----
1. Singly Linked List
   Node -> Next

2. Doubly Linked List
   Previous <- Node -> Next

3. Circular Linked List
   Last node -> First node


LINKED LIST vs PYTHON LIST
--------------------------
Linked List:
- Nodes connected using references
- No direct indexing
- Sequential access
- Extra memory for links

Python List:
- Supports direct indexing
- Dynamic array internally
- Fast access by index


TIME COMPLEXITY
---------------

Operation                  Linked List

Access by index               O(n)
Search                        O(n)
Insert at beginning           O(1)
Delete from beginning         O(1)
Insert after known node       O(1)
Delete after known node       O(1)
Traversal                     O(n)


ADVANTAGES
----------
- Dynamic size
- Easy insertion/deletion when position/node is known
- No requirement for contiguous memory


DISADVANTAGES
-------------
- No direct/random access
- Extra memory for references
- Searching is O(n)
- More complex than a normal Python list


IMPORTANT INTERVIEW POINT
-------------------------
Linked list nodes do not need to be stored next to
each other in memory.

The reference/link connects one node to another.
"""
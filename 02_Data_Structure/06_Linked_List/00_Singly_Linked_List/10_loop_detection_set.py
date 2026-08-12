# Detect a loop in linked list using set

# Crearting a singly linked list node bluprint
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# Creting nodes or node objects
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

# creting linked list

# creating head
head = node1

# linking node to next value
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = head

visited_node = set()

current = head

while current is not None:
    if current in visited_node:
        print("Loop detected")
        break

    visited_node.add(current)
    current = current.next

else:
    print("No loop found")

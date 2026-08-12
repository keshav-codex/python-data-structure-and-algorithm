# Delete last node of a linked list

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

if head is None:
    print("Empty linked list")

elif head.next is None:
    head.data = None
    head = None
    print("Linked list only had head and it's delated")

else:
    previous = head
    current = head.next
    
    while current.next is not None:
        previous = current
        current = current.next

    current.data = None # deleting last node
    previous.next = None # pointing second last 

    # printing linked list after delation
    current = head
    while current is not None:
        print(current.data)
        current = current.next
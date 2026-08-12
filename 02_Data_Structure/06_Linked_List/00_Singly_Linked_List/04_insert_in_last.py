# insert a node in last of linked list and print value

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

head = node1
node1.next = node2
node2.next = node3

if head is None:
    head = Node(40)

else:
    current = head
    while current.next is not None:
        current = current.next

    # creating a new list and adding to existing list
    inserted_node = Node(40) # new node created
    current.next = inserted_node # initial last node pointing to new node

    # Now printing linked list
    current = head

    while current is not None:
        print(current.data)
        current = current.next
# Insert a node in beginning of singly linked list and print it's value.

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

head = node1
node1.next = node2
node2.next = node3
node3.next = node4

# Inserting a node in begignning value having 60

inserted_node = Node(60)
inserted_node.next = head
head = inserted_node

# printing new linjed list

current = head

while current is not None:
    print(current.data)
    current = current.next

# Delete head of a linked list

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

if head is not None:
    # Deleting head
    target = head
    head = head.next
    target.next = None
    target.data = None

    if head is None:
        print("After deletion empty linked list")

    else:
        current = head
        while current is not None:
            print(current.data)
            current = current.next

else:
    print("Already Empty Linked List")
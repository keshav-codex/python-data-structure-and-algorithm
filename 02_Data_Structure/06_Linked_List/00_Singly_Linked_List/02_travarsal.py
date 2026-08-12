# create and traverse a singly linked list and print it's value.

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

# Travarsal

if head == None:
    print("empty linked list")

else:
    current = head
    count = 1

    while current is not None:
        print(f"Node no {count} : value is : {current.data}")
        count += 1
        current = current.next

        print(f"Total node : {count}")
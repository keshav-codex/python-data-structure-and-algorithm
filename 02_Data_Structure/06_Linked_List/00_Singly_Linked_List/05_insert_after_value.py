# insert a node only after a given value in linked list and print linked list

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

# Assuming for valid input

target_node = int(input("Enter value after which you want to insert node : "))
node_to_insert = int(input("Enter value to insert : "))

if head is None:
    print("Linked list not exist")

else:
    current = head
    inserted = False

    while current is not None:
        if current.data == target_node:
            inserted_node = Node(node_to_insert) #new node creating
            inserted_node.next = current.next   # new node points to what current used to point to
            current.next = inserted_node # current points to new node
            inserted = True
            break

        current = current.next

    if inserted:
        print("Insertion succesfull")
        current = head
        while current is not None:
            print(current.data)
            current = current.next

    else:
        print("Target value not found")
# Delete a target node in linked list and print final linked list

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

# Assuming for valid data type input
target = int(input("Input an interger node to delete: "))

deletion_done = False

if head is None:
    print("Empty linked list")

else:

    # searching for target to delete
    
    if head.data == target:
        target_node = head
        head.data = None
        deletion_done = True

        if head.next is not None:
            head = head.next
            target_node.next = None

        else:
            head = None
        
    else:
        previous = head
        current = head.next

        while current is not None:
            if current.data == target:
                current.data = None
                previous.next = current.next
                deletion_done = True
                break

            previous = current
            current = current.next

    # checking deletion done or not, if yes than also print remaining linked list
    if deletion_done:

        if head is None:
            print("Empty linked list")

        else:
            current = head
            print("Target deleted")
            print("Linked list after deletion")
            while current is not None:
                print(current.data)
                current = current.next

    else:
        print("Target not found")
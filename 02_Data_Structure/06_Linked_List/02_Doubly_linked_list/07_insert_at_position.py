# doubly linked list, insert at postion
class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


node1 = Node(10)
node2 = Node(30)
node3 = Node(40)

node1.next = node2
node2.prev = node1

node2.next = node3
node3.prev = node2

head = node1

position = 2
new_node = Node(20)

if position == 1:
    new_node.next = head
    new_node.prev = None
    if head is not None:
        head.prev = new_node
    head = new_node  

else:
    current = head

    for i in range(position - 2):
        current = current.next

    new_node.next = current.next
    new_node.prev = current

    current.next.prev = new_node
    current.next = new_node

    current = head

    while current is not None:
        print(current.data)
        current = current.next
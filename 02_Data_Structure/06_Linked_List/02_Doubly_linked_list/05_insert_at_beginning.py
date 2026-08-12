class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


node1 = Node(20)
node2 = Node(30)

node1.next = node2
node2.prev = node1

head = node1

new_node = Node(10)

new_node.next = head
head.prev = new_node

head = new_node

current = head

while current is not None:
    print(current.data)
    current = current.next
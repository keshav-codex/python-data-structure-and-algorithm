class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


node1 = Node(10)
node2 = Node(20)

node1.next = node2
node2.prev = node1

head = node1

new_node = Node(30)

current = head

while current.next is not None:
    current = current.next

current.next = new_node
new_node.prev = current

current = head

while current is not None:
    print(current.data)
    current = current.next
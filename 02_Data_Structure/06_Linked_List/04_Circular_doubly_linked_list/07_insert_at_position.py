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

node3.next = node1
node1.prev = node3

head = node1

position = 2
new_node = Node(20)

current = head

for i in range(position - 2):
    current = current.next

new_node.next = current.next
new_node.prev = current

current.next.prev = new_node
current.next = new_node

current = head

while True:
    print(current.data)
    current = current.next

    if current == head:
        break
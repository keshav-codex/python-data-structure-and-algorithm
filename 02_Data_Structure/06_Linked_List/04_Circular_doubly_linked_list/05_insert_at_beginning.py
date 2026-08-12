class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


node1 = Node(20)
node2 = Node(30)

node1.next = node2
node2.prev = node1

node2.next = node1
node1.prev = node2

head = node1

tail = head.prev

new_node = Node(10)

new_node.next = head
new_node.prev = tail

tail.next = new_node
head.prev = new_node

head = new_node

current = head

while True:
    print(current.data)
    current = current.next

    if current == head:
        break
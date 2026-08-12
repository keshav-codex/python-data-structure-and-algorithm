class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node1 = Node(20)
node2 = Node(30)

node1.next = node2
node2.next = node1

head = node1

new_node = Node(10)

current = head

while current.next != head:
    current = current.next

new_node.next = head
current.next = new_node
head = new_node

current = head

while True:
    print(current.data)
    current = current.next

    if current == head:
        break
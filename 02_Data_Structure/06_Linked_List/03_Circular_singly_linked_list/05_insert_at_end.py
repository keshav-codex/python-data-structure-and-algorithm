class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node1 = Node(10)
node2 = Node(20)

node1.next = node2
node2.next = node1

head = node1

new_node = Node(30)

current = head

while current.next != head:
    current = current.next

current.next = new_node
new_node.next = head

current = head

while True:
    print(current.data)
    current = current.next

    if current == head:
        break
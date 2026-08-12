class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.prev = node1

node2.next = node3
node3.prev = node2

node3.next = node1
node1.prev = node3

head = node1

target = 20

current = head
found = False

while True:
    if current.data == target:
        found = True
        break

    current = current.next

    if current == head:
        break

if found:
    print("Element Found")
else:
    print("Element Not Found")
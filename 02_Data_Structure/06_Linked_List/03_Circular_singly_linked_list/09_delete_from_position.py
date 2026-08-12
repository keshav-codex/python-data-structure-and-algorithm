class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node1

head = node1

position = 3

current = head

for i in range(position - 2):
    current = current.next

current.next = current.next.next

current = head

while True:
    print(current.data)
    current = current.next

    if current == head:
        break
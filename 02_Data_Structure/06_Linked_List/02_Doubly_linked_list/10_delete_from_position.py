class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.prev = node1

node2.next = node3
node3.prev = node2

node3.next = node4
node4.prev = node3

head = node1

position = 3

current = head

for i in range(position - 1):
    current = current.next

current.prev.next = current.next
current.next.prev = current.prev

current = head

while current is not None:
    print(current.data)
    current = current.next
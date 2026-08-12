class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


node1 = Node(10)

print("Previous :", node1.prev)
print("Data :", node1.data)
print("Next :", node1.next)
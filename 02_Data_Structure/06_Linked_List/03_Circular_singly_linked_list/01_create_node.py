class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node1 = Node(10)

print("Data :", node1.data)
print("Next :", node1.next)
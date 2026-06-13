class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

node1=Node(10)
node2=Node(20)
node3=Node(30)

node1.next=node2
node2.prev=node1
node2.next=node3
node3.prev=node2

current=node1
print("None",end="<->")
while current is not None:
    print(f'{current.data}<->',end="")
    current=current.next
print("None")
    
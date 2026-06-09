'''There is a singly-linked list head and we want to delete a node node in it.

You are given the node to be deleted node. You will not be given access to the first node of head.

All the values of the linked list are unique, and it is guaranteed that the given node node is not the last node in the linked list.

Delete the given node. Note that by deleting the node, we do not mean removing it from memory. We mean:

The value of the given node should not exist in the linked list.
The number of nodes in the linked list should decrease by one.
All the values before node should be in the same order.
All the values after node should be in the same order.'''

head = [4,5,1,9]
node = 5

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
def arr_to_ll(arr):
    if not arr:
        return None
    head=Node(arr[0])
    current=head
    for i in range(1,len(arr)):
        current.next=Node(arr[i])
        current=current.next
    return head

def print_ll(head):
    current=head
    while current is not None:
        print(current.data,end="->")
        current=current.next
    print("None")

#func to delete node
def deleteNode(node):
    node.data=node.next.data
    node.next=node.next.next

# Create linked list
h = arr_to_ll(head)

print("Before deletion:")
print_ll(h)

# Find node with value 5
current = h
while current is not None and current.data != node:
    current = current.next

# Delete that node
deleteNode(current)

print("After deletion:")
print_ll(h)
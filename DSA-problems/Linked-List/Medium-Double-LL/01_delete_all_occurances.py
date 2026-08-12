'''Given the head of a doubly linked list and an integer target.
Delete all nodes in the linked list with the value target and return the head of the modified linked list.'''
class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

def arr_to_ll(arr):
    if not arr:
        return None
    head=Node(arr[0])
    current=head
    
    for i in range(1,len(arr)):
        new_node=Node(arr[i])
        
        current.next=new_node
        new_node.prev=current
        current=current.next
        
    return head
def print_dll(head):
    current=head
    print("None",end="<->")
    while current:
        print(current.data,end="<->")
        current=current.next
    print("None")


def optimal(head):
    if not head:
        return None
  
    curr=head
    while curr:
        if target==curr.data:
            if curr==head:
                head=head.next
            next_node=curr.next
            prev_node=curr.prev
            
            if next_node:
                next_node.prev=prev_node
            if prev_node:
                prev_node.next=next_node
            curr=next_node 
        else: 
            curr=curr.next

    return head

l1=[1,1,2,3,1,4,1]
target=1
head=arr_to_ll(l1)
h=optimal(head)
print_dll(h)
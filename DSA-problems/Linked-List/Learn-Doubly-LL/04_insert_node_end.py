#Insert node at the end of DLL
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

def print_ll(head):
    curr=head
    while curr:
        print(curr.data,end="<->")
        curr=curr.next
    print("None")

def insert_node_end(head,value):
    if head is None:
        return None
    
    if value is None:
        return head
    new_node=Node(value)
    current=head
    while current.next:
        current=current.next
    
    current.next=new_node
    new_node.prev=current
    
    return head

head=arr_to_ll([1])
print_ll(head)
nh=insert_node_end(head,5)
print_ll(nh)
    
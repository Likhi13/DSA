#Insert node at the beginning of DLL
#Convert DLL to Array and Print

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
    while current:
        print(current.data,end="<->")
        current=current.next
    print("None")
    
def insert_node_beg(head,value):
    if value is None:
        return head
    
    if head is None:
        return None
    
    new_node=Node(value)
    
    head.prev=new_node
    new_node.next=head
    head=new_node
    
    return head

head=arr_to_ll([])
print_dll(head)
nh=insert_node_beg(head,None)
print_dll(nh)
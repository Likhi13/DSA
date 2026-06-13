#Insert a node at a given position

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

def insert_node_at_pos(head,pos,value):
    if value is None:
        return head 
    
    new_node=Node(value)
    
    if head is None:
        return new_node if pos==0  else None
    
    if pos==0:
        head.prev=new_node
        new_node.next=head
        head=new_node
        return head

    
    current=head
    count=0

    while current and count<pos-1:
        count+=1
        current=current.next
        
    if current is None:
        return head
    
    new_node.prev=current   
    new_node.next=current.next
    
    if current.next:
        current.next.prev=new_node

    current.next=new_node
    
    return head

head=arr_to_ll([1,2,3,4,5])
print_ll(head)
nh=insert_node_at_pos(head,0,0)
print_ll(nh)
    

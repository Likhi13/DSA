#Insert node at a given position

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
    
def insert_at_x(head,x,value):
    new_node=Node(value)
    
    if x==0:
        new_node.next=head
        head=new_node
        return head
    
    current=head
    count=0
    while current is not None and count < x-1:
        count+=1
        current=current.next
    
    if current is None:
        return head 
    
    new_node.next=current.next
    current.next=new_node
    
    return head

head=arr_to_ll([10,20])
print_ll(head)
head_now=insert_at_x(head,2,30)

print_ll(head_now)


    
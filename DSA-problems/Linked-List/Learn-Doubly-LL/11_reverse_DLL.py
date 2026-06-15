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

#Intuition: Swap the pointers 
def rev_dll(head):  
    current=head
    if head is None:
        return None
    while True:
        preserve_next=current.next
        current.next=current.prev  
        current.prev=preserve_next
        if current.prev is not None:
            current=current.prev
        else:
            break
    return current

head=arr_to_ll([1,2,3,4])
print_ll(head)
nh=rev_dll(head)
print_ll(nh)


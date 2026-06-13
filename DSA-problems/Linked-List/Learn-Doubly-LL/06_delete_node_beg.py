#delete node from the beginning

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

def del_node_beg(head):
    if head is None:
        return None
    if head.next is None:
        return None

    current=head.next
    current.prev=None 
    return current

head=arr_to_ll([1,2,3])
print_ll(head)
nh=del_node_beg(head)
print_ll(nh)
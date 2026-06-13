# delete node at end

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

def del_node_end(head):
    if  head is None or head.next is None:
        return None
    c=head
    while c.next.next :
        c=c.next
    c.next=None
    return head

head=arr_to_ll([1])
print_ll(head)
nh=del_node_end(head)
print_ll(nh)
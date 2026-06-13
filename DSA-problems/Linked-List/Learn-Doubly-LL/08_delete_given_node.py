#Delete given node from DLL

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

def delete_given_node(head,value):
    # none 
    if head is None:
        return None
    current=head
    if head.data==value:
        current=head.next
        if current:
            current.prev=None
        return current

    while current.next:
        if current.next.data==value:
            current.next=current.next.next
        # if next pointer exists
            if current.next:
                current.next.prev=current
            return head
        current=current.next
            
    return head
head=arr_to_ll([1,2,3,4])
print_ll(head)
nh=delete_given_node(head,2)
print_ll(nh)
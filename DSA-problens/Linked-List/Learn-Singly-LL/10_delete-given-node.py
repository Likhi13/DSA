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
    
def delete_node(head,x):
    if head is None:
        return None
    if head.data==x:
        head=head.next
        return head
    
    current=head
    while current.next is not None:
        if current.next.data==x:
            current.next=current.next.next
            return head
        current=current.next
        
    return head
head=arr_to_ll([1,5,7,8])
print_ll(head)
head_now=delete_node(head,9)
print_ll(head_now)
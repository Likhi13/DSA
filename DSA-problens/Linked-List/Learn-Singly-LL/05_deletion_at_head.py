#deletion at head in Linked List

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
    
def delete_head(head):
    if head is None:
        return None
    head=head.next
    return head

head=arr_to_ll([])
print_ll(head)
head_now=delete_head(head)
print_ll(head_now)
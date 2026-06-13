#insertion at tail in Linked List

class Node:
    def __init__(self,data):
        self.data=data 
        self.next=None

def arr_to_ll(arr):
    if not arr:
        return None
    head=Node(arr[0])
    current = head
    for i in range(1,len(arr)):
        current.next=Node(arr[i])
        current=current.next
    return head

def print_ll(head):
    current=head
    while current is not None:
        print(current.data, end="->")
        current=current.next
    print("None")

def insert_at_tail(head,value):
    new_node=Node(value)
    if head is None:
        head=new_node
        return head
    
    current=head
    while current.next is not None:
        current=current.next
    current.next=new_node
    return head

head=arr_to_ll([1,2,3])
print_ll(head)
head=insert_at_tail(head,4)
print_ll(head)
    
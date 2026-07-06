'''Given the head of a singly linked list, reverse the list, and return the reversed list.'''
head = [1,2,3,4,5]
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
        print(current.data, end="->")
        current=current.next
    print("none")
    
    
def reverse_ll(head):
    current=head
    prev=None
    while current:
        next_pointer=current.next 
        current.next=prev
        prev=current
        current=next_pointer
    return prev

nh=arr_to_ll(head)
print_ll(nh)
nnh=reverse_ll(nh)
print_ll(nnh)
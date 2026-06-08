#Deletion at end of Linked List

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

def delete_at_end(head):
    if head is None:
        return None
    if head.next is None:
        return None
    current=head
    while current.next.next is not None:
        current=current.next
    current.next=None
    return head


head=arr_to_ll([1,2,3,4,5,6,7,8,9])
print_ll(head)
head_now=delete_at_end(head)
print_ll(head_now)

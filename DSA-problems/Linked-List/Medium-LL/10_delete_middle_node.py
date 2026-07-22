'''You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.'''

head = [1,2]
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
    
    
def delete_node(head):
    if not head:
        return head
    if head.next is None:
        head=head.next
        return head
    fast=head
    slow=head
    before_middle=head
    while fast and fast.next:
        fast=fast.next.next
        before_middle=slow
        slow=slow.next
        
    before_middle.next=slow.next
    return head

#instead of taking another variable to store before node , skip one iteration
def delete_node_2(head):
    if not head or not head.next:
        return None

    slow=head
    fast=head
    
    #skip one iteration
    fast=fast.next
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    
    slow.next=slow.next.next
    return head

nh=arr_to_ll(head)
print_ll(nh)
nnh=delete_node_2(nh)
print_ll(nnh)
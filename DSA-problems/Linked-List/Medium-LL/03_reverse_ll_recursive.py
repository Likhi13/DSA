'''Given the head of a singly linked list, reverse the list, and return the reversed list.- Recursive way'''
head=[1,2,3,4,5]
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

#intuition: reversing the rest of the list first(go to last node), then fixing the current node's links while the recursion unwinds.
#5->4->None
#5->4->3->None
#5->4->3->2->None
#5->4->3->2->1->None
def reverse_ll(head):

    if head is None or head.next is None:
        return head
    
    new_head=reverse_ll(head.next)

    head.next.next=head
    head.next=None
    return new_head

nh=arr_to_ll(head)
print_ll(nh)
nnh=reverse_ll(nh)
print_ll(nnh)
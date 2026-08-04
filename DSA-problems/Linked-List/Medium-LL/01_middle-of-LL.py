'''Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def convert_arr(arr):
    #check for arr
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
    print(None)

head = [1,2,3,4,5,6,7]
#TC= O(n)+O(n/2)
def middle_of_ll(head):
    if head is None:
        return None
    
    current=head
    length=0
    while current:
        current=current.next
        length+=1

    mid=(length //2)+1

    current=head
    count=0
    while current:   
        if count==mid-1:
            return current
        current=current.next
        count+=1
#TC=O(n)
def middle_of_ll2(head):
    slow=head
    fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    return slow

h=convert_arr(head)
print_ll(h)
middle=middle_of_ll2(h)
print(middle)

'''slow
 |
 v
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7
 ^
 |
fast

IT:1
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7
     S    F
     
IT:2
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7
          S         F

IT:3
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7
               S              F
s returned '''
# 1->2->3->4->3->2->1
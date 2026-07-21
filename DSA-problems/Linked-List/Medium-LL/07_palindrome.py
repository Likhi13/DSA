'''Given the head of a singly linked list, return true if it is a palindrome or false otherwise.'''



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def create_linked_list(arr):
    if not arr:
        return None

    head = Node(arr[0])
    curr = head

    for x in arr[1:]:
        curr.next = Node(x)
        curr = curr.next

    return head


def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")


# Test Cases
head1 = create_linked_list([1,2,2,1])
# head2 = create_linked_list([1, 2, 3, 2, 1])
# head3 = create_linked_list([1, 2])
# head4 = create_linked_list([1])


def brute(head):
    if not head:
        return True
    last=head
    ar=[]
    while last:
        ar.append(last.data)
        last=last.next
    first=0
    lastt=len(ar)-1
    while first<lastt:
        if ar[first]!=ar[lastt]:
            return False
        first+=1
        lastt-=1
    return True


def optimal(head):
    if not head:
        return True
    if not head.next:
        return True
        
    current=head

    slow=current
    fast=current
    while fast and fast.next:

        slow=slow.next
        fast=fast.next.next
        
    if fast:
        slow=slow.next
        
    prev=None
    curr=slow
    while curr:
        next_p=curr.next
        curr.next=prev
        prev=curr
        curr=next_p

    first=head
    second=prev
    while second:
        if(second.data==first.data):
            second=second.next
            first=first.next
        else:
            return False
    return True

print(optimal(head1))   # Expected: True
# print(optimal(head2))   # Expected: True
# print(optimal(head3))   # Expected: False
# print(optimal(head4))   # Expected: True
    
    
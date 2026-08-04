'''Given the head of a linked list, return the list after sorting it in ascending order.'''
head = [4,6,8,2,3]

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
    
def brute(head):
    arr=[]
    current=head
    while current:
        arr.append(current.data)
        current=current.next
        
    sorted_arr=sorted(arr)
    head=Node(sorted_arr[0])
    current=head
    for i in range(1,len(sorted_arr)):
        current.next=Node(sorted_arr[i])
        current=current.next
    return head




def find_middle(head):
    fast=head.next
    slow=head
    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next
    return slow
def merge_sort(head):
    if head is None or head.next is None:
        return head
    
    middle=find_middle(head)
    
    right_head=middle.next
    middle.next=None
    left_head=head
    
    left_head=merge_sort(left_head)
    right_head=merge_sort(right_head)

    merged_list=merge(left_head,right_head)
    print_ll(merged_list)
    return merged_list

def merge(head1,head2):
    left_head=head1
    right_head=head2
    dummy=Node(-1)
    temp=dummy
    while left_head and right_head:
        if left_head.data<=right_head.data:
            temp.next=left_head
            temp=left_head
            left_head=left_head.next
        else:
            temp.next=right_head
            temp=right_head
            right_head=right_head.next
    if left_head:
        temp.next=left_head
    else:
        temp.next=right_head
    return dummy.next

            
    
nh=arr_to_ll(head)
print_ll(nh)
nnh=merge_sort(nh)
print_ll(nnh)
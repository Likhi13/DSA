#Length if linked list

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
    print(current)
    print("None")
    
def length_of_ll(head):
    if head is None:
        return 0
    current=head
    count=0
    while current is not None:
        count+=1
        current=current.next
    return count


head=arr_to_ll([1,2,3,4,5])
print_ll(head)
print(length_of_ll(head))
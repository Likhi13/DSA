#converting arr to linnked list
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

head=convert_arr([1,2,3,4,5,6])
print_ll(head)
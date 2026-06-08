#search a given node

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
    
def search_node(head,target):
    current=head
    while current is not None:
        if current.data == target:
            return True
        current=current.next
    return False

head=arr_to_ll([6,8,5,3,9])
print_ll(head)
x=search_node(head,0)
print(x)
    
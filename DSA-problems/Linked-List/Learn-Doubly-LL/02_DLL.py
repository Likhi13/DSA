#Convert DLL to Array and Print

class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

def arr_to_ll(arr):
    if not arr:
        return None
    head=Node(arr[0])
    current=head
    
    for i in range(1,len(arr)):
        new_node=Node(arr[i])
        
        current.next=new_node
        new_node.prev=current
        current=current.next
        
    return head
def print_dll(head):
    current=head
    print("None",end="<->")
    while current:
        print(current.data,end="<->")
        current=current.next
    print("None")

head=arr_to_ll([1,2,3,4,5,6])
print_dll(head)
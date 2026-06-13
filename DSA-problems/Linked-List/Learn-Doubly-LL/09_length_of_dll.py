#length of dll
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

def print_ll(head):
    curr=head
    while curr:
        print(curr.data,end="<->")
        curr=curr.next
    print("None")
def length(head):
    count=0
    current=head
    while current:
        current=current.next
        count+=1
    return count

head=arr_to_ll([1,2,3,4,5])
print(length(head))
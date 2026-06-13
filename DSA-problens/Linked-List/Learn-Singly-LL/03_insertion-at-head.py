#insertion at head in a Linked List
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
    
def insert_at_head(head,value):
    new_node=Node(value)  
    new_node.next=head
    return new_node

def print_ll(head):
    current=head
    while current is not None:
        print(current.data, end="->")
        current=current.next
    print("none")

    
head=arr_to_ll([1,2,3])
print_ll(head)
head_now=insert_at_head(head,0)
print_ll(head_now)

        
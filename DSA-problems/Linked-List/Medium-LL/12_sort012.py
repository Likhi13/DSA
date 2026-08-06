'''Given the head of a singly linked list consisting of only 0, 1 or 2.
Sort the given linked list and return the head of the modified list.
Do it in-place by changing the links between the nodes without creating new nodes.'''

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



def brute(head):
    if not head:
        return None
    arr=[]
    temp=head
    while temp:
        arr.append(temp.data)
        temp=temp.next
    
    arr.sort()
    print("arr",arr)
    head=create_linked_list(arr)
    return head


def optimal(head):
    
    dummy_0=Node(-1)
    dummy_1=Node(-1)
    dummy_2=Node(-1)
    tail_0=dummy_0
    tail_1=dummy_1
    tail_2=dummy_2
    
    temp=head
    while temp:
        nxt=temp.next
        temp.next=None
        
        if temp.data==0:
            tail_0.next=temp
            tail_0=tail_0.next

        elif temp.data==1:
            tail_1.next=temp
            tail_1=tail_1.next
        else:
            tail_2.next=temp
            tail_2=tail_2.next
            
        temp=nxt
        
    tail_0.next=dummy_1.next if dummy_1.next else dummy_2.next
    tail_1.next=dummy_2.next
    tail_2.next=None
        
    if not dummy_0.next:
        dummy_0.next=dummy_1.next if dummy_1.next else dummy_2.next
        
    return dummy_0.next

        
            
head=[]
nh=create_linked_list(head)
print_list(nh)
nnh=optimal(nh)
print_list(nnh)
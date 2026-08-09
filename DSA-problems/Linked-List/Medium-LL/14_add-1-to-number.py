'''Given the head of a singly linked list representing a positive integer number. Each node of the linked list represents a digit of the number, with the 1st node containing the leftmost digit of the number and so on. The task is to add one to the value represented by the linked list and return the head of a linked list containing the final value.'''

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
    temp=head
    arr=[]
    while temp:
        arr.append(temp.data)
        temp=temp.next
    
    print("num:",arr)
    num=0
    for digit in arr:
        num=num*10+digit
    print(num)
    added_num=str(num+1)
    arr=[]
    for s in added_num:
        arr.append(int(s))
    
    print("num after",arr)
    head=create_linked_list(arr)
    return head

def reverse_ll(head):
    curr=head
    prev=None
    while curr:
        next_node=curr.next
        curr.next=prev
        prev=curr
        curr=next_node
    return prev
        
def better(head):
    last=reverse_ll(head)
    temp=last
    carry=1
    while temp:
        temp.data=temp.data+carry
        if temp.data<10:
            break
        else:
            temp.data=0
            carry=1
        temp=temp.next
    head=reverse_ll(last)
    if carry==1:
        new_node=Node(1)
        new_node.next=head
        return new_node
    return head
        
def helper(head):
    if not head:
        return 1
    carry=helper(head.next)
    head.data=head.data+carry
    if (head.data) <10:
        return 0
    head.data=0
    return 1

def optimal(head):
    carry=helper(head)
    if carry==1:
        new_node=Node(1)
        new_node.next=head
        return new_node
    return head
        
    
    
num=[9]
head=create_linked_list(num)
print_list(head)
new_head=brute(head)
print_list(new_head)
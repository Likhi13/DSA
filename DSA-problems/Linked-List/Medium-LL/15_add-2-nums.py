'''You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.'''

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

def optimal(h1,h2):
    dummy=Node(-1)
    t1=h1
    t2=h2
    carry=0
    temp=dummy
    while t1 or t2: 
        if t1 and t2:
            total=t1.data+t2.data+carry
            t1=t1.next
            t2=t2.next
        elif t1:
            total=t1.data+carry
            t1=t1.next
        else:
            total=t2.data+carry
            t2=t2.next
        carry=total//10
        new_node=Node(total%10)
        temp.next=new_node
        temp=temp.next
    if carry>0:
        new_node=Node(1)
        temp.next=new_node
    return dummy.next



l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
h1=create_linked_list(l1)
h2=create_linked_list(l2)
head=optimal(h1,h2) 
print_list(head)
    
        
        

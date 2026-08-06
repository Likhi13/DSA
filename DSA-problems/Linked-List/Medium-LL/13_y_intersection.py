'''Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.
'''

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

listA = [1,9,1,2,4]
listB = [3,2,4]

#TC= O(n+m) SC=o(n)
def brute(head1,head2):
    hashmap={}
    
    temp=head1
    while temp:
        hashmap[temp]=1
        temp=temp.next
        
    temp=head2
    while temp:
        if temp in hashmap:
            return temp
        temp=temp.next
    return temp

#TC=o(n)+o(2n) Sc=o(1)
def collisionNode(head1,head2,d):
    temp1=head1
    temp2=head2
    
    while d!=0:
        temp1=temp1.next
        d-=1

    while(temp1!=temp2):
        temp1=temp1.next
        temp2=temp2.next
    return temp1

def better(head1,head2):
    temp1=head1
    temp2=head2
    n1=0
    n2=0
    while temp1:
        n1+=1
        temp1=temp1.next
    while temp2:
        n2+=1
        temp2=temp2.next
    if n1>n2:

        return collisionNode(head1,head2,n1-n2)
    
    else:
        return collisionNode(head2,head1,n2-n1)

def optimal(head1,head2):
    if not head1 or not head2:
        return None
    temp1=head1
    temp2=head2
    while(temp1!=temp2):
        temp1=temp1.next
        temp2=temp2.next

        if not temp1:
            temp1=head2
        if not temp2:
            temp2=head1 
    return temp1
head1=create_linked_list(listA)
head2=create_linked_list(listB)
print_list(head1)
print_list(head2)
ans=better(head1,head2)
print(ans)
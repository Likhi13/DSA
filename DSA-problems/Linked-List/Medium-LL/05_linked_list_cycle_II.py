'''Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.'''

head = [3,2,0,-4]

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def create_linked_list(arr, pos):
    if not arr:
        return None

    nodes = [Node(x) for x in arr]


    for i in range(len(arr) - 1):
        nodes[i].next = nodes[i + 1]

  
    if pos != -1:
        nodes[-1].next = nodes[pos]

    return nodes[0]



arr = [3, 2, 0, -4]
pos = 1        # tail connects to node with value 2

head = create_linked_list(arr, pos)


def cycle1(head):
    curr = head
    hashmap={}
    count=0
    while curr:
        if curr in hashmap:
            break
        hashmap[curr]=count
        count+=1
        curr = curr.next

    if curr in hashmap:
        return curr
    return -1

#TC=O(n) SC=O(1)
def optimal(head):
    slow=head
    fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if(slow==fast):
            slow=head
            while slow!=fast:
                slow=slow.next
                fast=fast.next
            return slow
    return -1

head=create_linked_list(arr,pos)
print(cycle1(head))
print(optimal(head))
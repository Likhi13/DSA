'''Given the head of a linked list,
remove the nth node from the end of the list and return its head'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    #tc=O(2n) sc=o(1)
    def removeNthFromEnd(self, head, n):
        # Write your solution here
        if n <=0:
            return head
        
        current=head
        length=0
        while current:
            length+=1
            current=current.next
            
        if n > length:
            return head

        count = length - n
        
        if count==0:
            head=head.next
            return head
        
        current=head
        while current and count>1:
            current=current.next 
            count-=1
            
        if current.next:
            current.next=current.next.next
        return head
    def removeNthFromEndOptimal(self,head,n):
        if not head:
            return None
        fast=head
        for _ in range(0,n):
            fast=fast.next
            
        if fast is None:
            head=head.next
            return head
        
        slow=head
        while fast.next is not None:
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next
        return head
            
# ---------- Helper Functions ----------

def build_linked_list(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    curr = head

    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next

    return head


def print_linked_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> " if curr.next else "")
        curr = curr.next
    print()


# ---------- Test ----------

arr = [1, 2, 3, 4, 5]
n = 2

head = build_linked_list(arr)

print("Original:")
print_linked_list(head)

sol = Solution()
new_head = sol.removeNthFromEndOptimal(head, n)

print(f"After removing {n}th node from end:")
print_linked_list(new_head)
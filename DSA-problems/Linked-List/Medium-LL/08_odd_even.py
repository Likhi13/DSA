'''Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList1(self, head):
        if head is None:
            return None
        arr=[]
        current=head
        
        while current:
            arr.append(current)
            current=current.next
        new_arr=[]
        for i in range(len(arr)):
            if i % 2==0:
                new_arr.append(arr[i])
        
        for i in range(len(arr)):
            if i%2!=0:
                new_arr.append(arr[i])
        
        head = new_arr[0]
        curr=head       
        for i in range(1,len(new_arr)):
            curr.next=new_arr[i]
            curr=curr.next
        curr.next=None

        return head
    
    def oddEvenList(self,head):
        if not head:
            return None
        if not head.next:
            return head
        
        odd=head
        even=head.next
        store_even_head=head.next
        while even and even.next:
            odd.next=odd.next.next
            even.next=even.next.next
            odd=odd.next
            even=even.next
        
        odd.next=store_even_head
        if even:
            even.next=None
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

arr = [1,2,3,4]
head = build_linked_list(arr)

print("Original:")
print_linked_list(head)

sol = Solution()
new_head = sol.oddEvenList(head)

print("After Reordering:")
print_linked_list(new_head)

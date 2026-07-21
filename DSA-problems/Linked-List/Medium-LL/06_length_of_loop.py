#to count length of loop after 
# 1. detect a loop 
# 2. move fast pointer 1 step ahead and start counting until fast meets slow again 
def length_of_loop(head):
    slow=head
    fast=head

    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next

        if(slow==fast):
            count=1
            fast=fast.next
            while slow!=fast:
                fast=fast.next
                count+=1
            return count
    return 0
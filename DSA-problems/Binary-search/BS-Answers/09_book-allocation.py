'''Given an array nums of n integers,
where nums[i] represents the number of pages in the i-th book,
and an integer m representing the number of students,
allocate all the books to the students so that each student gets at least one book,
each book is allocated to only one student, and the allocation is contiguous.

Allocate the books to m students in such a way that the maximum number of pages assigned to a student is minimized.
If the allocation of books is not possible, return -1.'''
books = [12, 34, 67, 90]
s=2
def book_allocation_possible(books,p,s):
    students=1
    sum_pages=0
    for i in range(len(books)):
        sum_pages+=books[i]
        if sum_pages>p:
            sum_pages=books[i]
            students+=1
    if students<=s:
        return True
# tc= O(n * sum(books))                
def brute(books,s):
    #range max(books)->sum(pages)
    low=max(books)
    high=sum(books)
    for p in range(low,high+1):
        if book_allocation_possible(books,p,s):
            return p
    return -1
print(brute(books,s))

# tc= O(n * log(sum(books)))
def optimal(books,s):
    low=max(books)
    high=sum(books)
    while low<=high:
        mid=low+(high-low)//2
        if book_allocation_possible(books,mid,s):
            high=mid-1
        else:
            low=mid+1
    return low
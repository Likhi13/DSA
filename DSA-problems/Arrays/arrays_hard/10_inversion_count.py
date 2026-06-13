'''Given an integer array nums. Return the number of inversions in the array.
Two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.
It indicates how close an array is to being sorted.
A sorted array has an inversion count of 0.
An array sorted in descending order has maximum inversion.'''

nums = [2, 3, 7, 1, 3, 5]

def brute(nums):
    count=0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]>nums[j] and i<j:
                count+=1
    return count
# print(brute(nums))

# TC=O(N LOG N) SC=O(N)
# couting works:?
# left_count  = optimalms(nums, l, mid)
# right_count = optimalms(nums, mid+1, u)
# merge_count = m(nums, l, mid, u)

# count = left_count + right_count + merge_count
# return count
def optimalms(nums,l,u):
    count=0
    if l<u:
        mid=(l+u)//2
        # persistance for keeping the count value
        # left count
        count+=optimalms(nums,l,mid)
        # right count
        count+=optimalms(nums,mid+1,u)
        # actual val reeeturned is  here  right?
        count+=m(nums,l,mid,u)
    return count
# During merge, when a right element is smaller than a left element
# it forms inversions with all remaining elements in the left array.
def m(nums,l,mid,u):
    count=0
    left=nums[l:mid+1]
    right=nums[mid+1:u+1]
    i=0
    j=0
    k=l
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            nums[k]=left[i]
            i+=1
        else:
            nums[k]=right[j]
            j+=1
            count+=len(left)-i
        k+=1
    while i<len(left):
        nums[k]=left[i]
        k+=1
        i+=1
    while j<len(right):
        nums[k]=right[j]
        k+=1
        j+=1
    return count
        
def run(nums):
    l=0
    u=len(nums)-1
    c=optimalms(nums,l,u)
    return c
print(run(nums))

'''Given an integer array nums, return the number of reverse pairs in the array.

A reverse pair is a pair (i, j) where:

0 <= i < j < nums.length and
nums[i] > 2 * nums[j].'''

nums = [1,3,2,3,1]
def brute(nums):
    count=0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]>2*nums[j]:
                count+=1
    return count
# print(brute(nums)) 

# INTUITION:
# For each nums[i] in left half:
# Move j in right half only forward
# Find how many nums[j] satisfy:
# nums[i] > 2 * nums[j]
# Because right half is sorted:
# Once condition fails, it will fail for all further j
# once condition passes for a far elemnet in j, it means it passed for all before elements in j too, as both are sorted
# hence we don't set j back to 0 and keep moving j fwd and keep adding current count of j to "count"
def optimalms(nums,l,u):
    count=0
    if l<u:
        mid=(l+u)//2
        count+=optimalms(nums,l,mid)
        count+=optimalms(nums,mid+1,u)
        count+=m(nums,l,mid,u)
    return count

def m(nums,l,mid,u):
    count=0
    j=mid+1
    for i in range(l,mid+1):
        while j<=u and nums[i] > 2*nums[j]:
            j+=1
        count+=(j-(mid+1))
    
    left=nums[l:mid+1]
    right=nums[mid+1:u+1]

    i=j=0
    k=l

    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            nums[k]=left[i]
            i+=1
        else:
            nums[k]=right[j]
            j+=1
        k+=1
    while i<len(left):
        nums[k]=left[i]
        i+=1
        k+=1
    while j<len(right):
        nums[k]=right[j]
        j+=1
        k+=1
    return count

def run(nums):
    l=0
    u=len(nums)-1
    c=0
    c=optimalms(nums,l,u)
    return c
# print(run(nums))

# optimal practice
def sort(nums,l,u):
    count=0
    if l<u:
        mid=(l+u)//2
        count+=sort(nums,l,mid)
        count+=sort(nums,mid+1,u)
        count+=pm(nums,l,mid,u)
    return count

def pm(nums,l,mid,u):
    count=0
    j=mid+1
    for i in range(l,mid+1):
        while j<=u and nums[i]> 2*nums[j]:
            j+=1
        count+=(j-(mid+1))
        
    left=nums[l:mid+1]
    right=nums[mid+1:u+1]
    i=j=0
    k=l
    # here left and right are sorted
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            nums[k]=left[i]
            i+=1
        else:
            nums[k]=right[j]
            j+=1
        k+=1
    while i<len(left):
        nums[k]=left[i]
        i+=1
        k+=1
    while j<len(right):
        nums[k]=right[j]
        j+=1
        k+=1
    return count
def prun(nums):
    count=0
    l=0
    u=len(nums)-1
    count=sort(nums,l,u)
    return count
print(prun(nums))
            
        
        
'''Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Return the kth positive integer that is missing from this array.'''
arr = [2,3,4,7,11]
k = 2
#sc=o(1)->for all soln
# tc=o(n^2)
def brute(nums,k):
    count=0
    low=1
    high=max(nums)+k

    for i in range(low,high+1):
        if i not in nums:
            count+=1
        if count==k:
            return i
print(brute(arr,k))

# tc=o(n)
# If a number <= k exists in the array, then it cannot be counted as missing.
# So the kth missing number gets pushed one step ahead, hence k += 1.
def better(nums,k):
    
    for i in range(len(nums)):
        if nums[i]<=k:
            k+=1
        else:
            break
    return k

print(better(arr,k))

# tc=o(log n)
#using binary search         
# At index mid, compare how many numbers are missing till there.
# missing count= (the number which is there - actual number which should be there)
# Missing count till mid is: arr[mid]−(mid+1) 
# index: 0 1 2 3 4 
#arr   : 2 3 4 7 11
#missin: 1 1 1 3 6

# If missing count < k, move right.
# Else, move left because the kth missing lies before or at mid.

def optimal(nums,k):
    low=0
    high=len(nums)-1
    while low<=high:
        mid=low+(high-low)//2
        missing=arr[mid]-(mid+1)
        if missing< k:
            low=mid+1
        #missing >=k
        else:
            high=mid-1
    
    return high+1+k
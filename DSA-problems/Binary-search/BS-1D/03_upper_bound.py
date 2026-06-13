'''
Given a sorted array of nums and an integer x, write a program to find the upper bound of x.
The upper bound of x is defined as the smallest index i such that nums[i] > x.
If no such index is found, return the size of the array.'''
nums = [1,2,2,3]
x = 2
def brute(nums,x):
    ub=len(nums)
    for i in range(len(nums)):
       if nums[i]>x:
           ub=i
           break
    return ub
print(brute(nums,x)) 

def optimal(nums,x):
    ub=len(nums)
    low=0
    high=len(nums)-1
    while low<=high:
        mid=(low+(high-low)//2)
        if nums[mid]>x:
            ub=mid
            high=mid-1
        else:
            low=mid+1
    return ub
print(optimal(nums,x))
    

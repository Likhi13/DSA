'''Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Note that the product of an array with a single element is the value of that element.'''
nums =  [2, 4,-3]
# TC= O(N^2) SC=O(1)
def brute(nums):
    max_p=float('-inf')
    for i in range(len(nums)):
        prod=nums[i]
        max_p=max(prod,max_p)
        for j in range(i+1,len(nums)):
            prod*=nums[j]
            max_p=max(prod,max_p)
    return max_p
print(brute(nums))

def optimal(nums):
    prefix=1
    suffix=1
    max_p=float('-inf')
    for i in range(len(nums)):
        prefix*=nums[i]
        suffix*=nums[len(nums)-1-i]
        max_p=max(max_p,max(prefix,suffix))
        if prefix==0:
            prefix=1
        if suffix==0:
            suffix=1

    return max_p
print(optimal(nums))  
            
        
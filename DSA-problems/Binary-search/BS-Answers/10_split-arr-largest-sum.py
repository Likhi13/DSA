'''Given an integer array nums and an integer k,
split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

Return the minimized largest sum of the split.
A subarray is a contiguous part of the array.'''

nums = [7,2,5,10,8]
k = 2

def is_possible(nums,ls,k):
    sum_el=0
    count_arr=1
    for i in range(len(nums)):
        sum_el+=nums[i]
        if sum_el>ls:
            count_arr+=1
            sum_el=nums[i]
    if count_arr<=k:
        return True
    else:
        return False
    
# tc =  O(n *sum(nums))
def brute(nums,k):
    low=max(nums)
    high=sum(nums)
    for ls in range(low,high+1):
        if is_possible(nums,ls,k):
            return ls
    return -1
print(brute(nums,k))

# tc= O(n log(sum(nums)))
def optimal(nums,k):
    low=max(nums)
    high=sum(nums)
    while low<=high:
        mid=low+(high-low)//2
        if is_possible(nums,mid,k):
            high=mid-1
        else:
            low=mid+1
        
    if low >=0 and low<=sum(nums):
        return low
    return -1
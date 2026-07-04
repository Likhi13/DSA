'''Easy
Topics
premium lock icon
Companies
Hint
Given an array of positive integers nums, return the maximum possible sum of an strictly increasing subarray in nums.

A subarray is defined as a contiguous sequence of numbers in an array.
'''
nums = [10,20,30,5,10,50]

def asc_sum(nums):
    sum=nums[0]
    max_sum=sum
    for i in range(1,len(nums)):
        if nums[i-1]<nums[i]:
            sum+=nums[i]
            max_sum=max(sum,max_sum)
        else:
            sum=nums[i]
    return max_sum
print(asc_sum(nums))

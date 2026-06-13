import math
'''Given an array of nums and an threshold,
we will choose a divisor,
divide all the array by it,
and sum the division's result.
Find the smallest divisor such that the result mentioned above is less than or equal to threshold.

Each result of the division is rounded to the nearest integer greater than or equal to that element. (For example: 7/3 = 3 and 10/2 = 5).'''
nums = [1,2,5,9]
threshold = 6

#TC= O(n*max(arr))
def brute(nums,th):

    for d in range(1,nums[len(nums)-1]+1):
        sum=0
        for n in range(len(nums)):
            res=nums[n]/d
            sum+=math.ceil(res)
        print(sum)
        if sum<=th:
            return d
# print(brute(nums,threshold))

def optimal(nums,th):
    low=1
    high=max(nums)
    smid=float('inf')
    while low<=high:
        mid=(low+(high-low)//2)
        sum=0
        for n in range(len(nums)):
            res=nums[n]/mid
            sum+=math.ceil(res)    
        if sum<=th:
            smid=mid
            high=mid-1
        else:
            low=mid+1   
    return smid
print(optimal(nums,threshold)) 
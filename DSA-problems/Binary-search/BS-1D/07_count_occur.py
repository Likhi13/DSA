'''You are given a sorted array of integers arr and an integer target. Your task is to determine how many times target appears in arr.
Return the count of occurrences of target in the array.'''
arr = [0, 0, 1, 1, 1, 2, 3]
target = 1
def brute(nums,target):
    count=0
    for i in range(len(nums)):
        if nums[i]==target:
            count+=1
    return count
print(brute(arr,target))

def optimal(nums,target):
    low=0
    high=len(nums)-1
    lb=len(nums)
    while low<=high:
        mid=(low+(high-low)//2)
        if nums[mid]>=target:
            lb=mid
            high=mid-1
        else:
            low=mid+1

    low=0
    high=len(nums)-1
    ub=len(nums)
    while low<=high:
        mid=(low+(high-low)//2)
        if nums[mid]>target:
            ub=mid
            high=mid-1
        else:
            low=mid+1
    if lb==len(nums) or nums[lb]!=target:
        return 0
    first=lb
    last=ub-1
    #or simply ub-lb->count
    return last-first+1
# print(optimal(arr,target))

'''Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.'''
nums = [5,7,7,8,8,10]
target = 8
def brute(nums,target):
    first,last=-1,-1
    
    for i in range(len(nums)):
        if nums[i]==target:
            if first==-1:
                first=i
            last=max(i,last)
        
    return first,last

print(brute(nums,target))

def optimal(nums,target):
    low=0
    high=len(nums)-1

    min_first,max_last=-1,-1
    #searching for first occur have to keep searching in the left search space and elominate right search space
    while low<=high:
        mid=(low+(high-low)//2)
        if nums[mid]==target:
            min_first=mid
            high=mid-1
        #right search for >= elements
        elif nums[mid]<target:
            low=mid+1
        #greater than target, we ant to search for left for least index
        else:
            high=mid-1
    
    low=0
    high=len(nums)-1
    #searching for last occur have to keep searching in right space, cut left space
    while low<=high:
        mid=(low+(high-low)//2)
        if nums[mid]==target:
            max_last=mid
            low=mid+1
        #left search for <= elements
        elif nums[mid]>target:
            high=mid-1
        #less than tareget->we want greater index so right space search
        else:
            low=mid+1
    return min_first,max_last
print(optimal(nums,target))
            
#usig lb and ub
#lb >= so we want fetch->ans
#ub > so we fetch ub
#first check for lb==len(arr)(hypothetical case where takes the last+1 index) || nums[lb]!=target
#any fo above case fails means there is no lb and ub too, so return -1,-1
#if lb exists then last occur=ub-1
def optimal2(nums,target):
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
        return -1,-1
    return lb,ub-1
print(optimal2(nums,target))
    
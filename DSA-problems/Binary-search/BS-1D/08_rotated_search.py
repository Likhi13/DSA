'''There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.'''
nums = [4,5,6,7,0,1,2]
target = 0
def brute(nums,target):
    for i in range(len(nums)):
        if nums[i]==target:
            return i
    return -1
# print(brute(nums,target))

#3(log n)
def optimal(nums,target):
    low=0
    high=len(nums)-1
    #pivot- assume mid as pivot
    #why comapre with high-> (big values, pivot, small values)
    pivot=-1
    while low<=high:
        mid=(low+(high-low)//2)
        if nums[mid]>nums[high]:
            low=mid+1
        elif nums[mid]<=nums[high]:
            pivot=mid
            high=mid-1
    low=0
    high=pivot-1

    while low<=high:
        mid=(low+(high-low)//2)
        if nums[mid]<target:
            low=mid+1
        elif nums[mid]>target:
            high=mid-1
        else:
            return mid
    low=pivot
    high=len(nums)-1
    while low<=high:
        mid=(low+(high-low)//2)
        if nums[mid]<target:
            low=mid+1
        elif nums[mid]>target:
            high=mid-1
        else:
            return mid
    return -1
            
# print(optimal(nums,target))
#o(log n)
def optimal2(nums,target):
    low=0
    high=len(nums)-1
    while low<=high:
        mid=(low+(high-low)//2)
        #found
        if target==nums[mid]:
                    return mid
        #left half is sorted
        elif nums[low]<=nums[mid]:
            #if target bwn low and mid->keep searching in left
            if nums[low]<=target<nums[mid]:
                high=mid-1
            #elase-> search in right
            else:
                low=mid+1
        # right half is sorted        
        else:
            #if target bwn mid and high ->leep searching in right 
            if nums[mid]<target<=nums[high]:
                low=mid+1
            #if not then search in left  
            else:
                high=mid-1

    return -1
print(optimal2(nums,target))
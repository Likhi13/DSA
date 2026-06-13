'''Given a sorted array nums and an integer x. Find the floor and ceil of x in nums. The floor of x is the largest element in the array which is smaller than or equal to x. The ceiling of x is the smallest element in the array greater than or equal to x. If no floor or ceil exists, output -1.'''
nums = [5,7,7,8,8,10]
x=8
def brute(nums,x):
    ceil,floor=-1,-1
    for i in range(len(nums)):
        if nums[i]<=x:
            floor=nums[i]
    for i in range(len(nums)):
        if nums[i]>=x:
            ceil=nums[i]
            break
    return ceil,floor
# print(brute(nums,x))

#floor= largest element (smaller or = to x)
#ceil= smallest element(larger or = to x) == lower bound
#tc= o(logn)+o(logn) sc=0(1)
def optimal(nums,x):
    floor=-1
    ceil=-1
    low=0
    high=len(nums)-1
    while low<=high:
        mid=(low+(high-low)//2)
        if nums[mid]<=x:
            floor=nums[mid]
            low=mid+1
        else:
            high=mid-1
    low=0
    high=len(nums)-1
    while low<=high:
        mid=(low+(high-low)//2)
        if nums[mid]>=x:
            ceil=nums[mid]
            high=mid-1
        else:
            low=mid+1
    return ceil,floor
print(optimal(nums,x))

#floor= largest element (smaller or = to x)
#ceil= smallest element(larger or = to x) == lower bound
def optimal_combined(nums,x):
    ceil,floor=-1,-1
    low=0
    high=len(nums)-1
    while low<=high:
        mid=(low+(high-low)//2)
        if nums[mid]==x:
            ceil=nums[mid]
            floor=nums[mid]
            return ceil,floor
        elif nums[mid]>x:
            ceil=nums[mid] 
            high=mid-1
        else:
            floor=nums[mid]
            low=mid+1
    return ceil,floor
# print(optimal_combined(nums,x))
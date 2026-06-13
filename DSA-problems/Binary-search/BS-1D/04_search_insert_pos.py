''''Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.'''
nums = [1,3,5,6]
target = 5
#using lowerbound+ bs
def optimal(nums,target):
    pos=len(nums)
    low=0
    high=len(nums)-1
    while low<=high:
        mid=(low+(high-low)//2)
        if nums[mid]>=target:
            pos=mid
            high=mid-1
        else:
            low=mid+1
    return pos
print(optimal(nums,target))
    
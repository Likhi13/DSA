'''Given an integer array nums of size n, sorted in ascending order with distinct values. The array has been right rotated an unknown number of times, between 0 and n-1 (including). Determine the number of rotations performed on the array.'''
nums = [4, 5, 6, 7, 0, 1, 2, 3]
def optimal(nums):
    low=0
    high=len(nums)-1
    smallest=float('inf')
    ind=-1
    while low<=high:
        mid=(low+(high-low)//2)
        #if low<=high means we got the ans(alrdy sorted) caz here [4,5,6,0,1,2], low cant be less than high unless it came to 0-1/0-2
        if nums[low]<=nums[high]:
            if nums[low]<smallest:
                return low
        #search for sorted part
        if nums[low]<=nums[mid]:
            if nums[low]<smallest:
                smallest=nums[low]
                ind=low
            low=mid+1
        else:
            high=mid-1
            if nums[mid]<smallest:
                smallest=nums[mid]
                ind=mid
    return ind
print(optimal(nums))
    
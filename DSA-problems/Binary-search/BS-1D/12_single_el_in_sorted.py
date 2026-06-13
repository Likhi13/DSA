'''You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.'''
nums =[1,1,2,2,3,3,4,4,5,6,6,7,7]
def brute(nums):
    unique=0
    for i in range(len(nums)):
        unique^=nums[i]
    return unique
# print(brute(nums))

def optimal(nums):
    if len(nums)==1:
        return nums[0]
    low=0
    high=len(nums)-1
    while low<=high:
        mid=(low+(high-low)//2)
        if mid+1 <len(nums) and mid-1 >=0:
            if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
                return nums[mid]
            if mid%2==0:
                if nums[mid-1]==nums[mid]:
                    high=mid-1
                elif nums[mid]==nums[mid+1]:
                    low=mid+1
            else:
                if nums[mid-1]==nums[mid]:
                    low=mid+1
                elif  nums[mid]==nums[mid+1]:
                    high=mid-1
        else:
            return nums[mid]
print(optimal(nums))
#cleaner soln
def op2(nums):
    n=len(nums)
    #checking for edge case n=1
    if n==1:
        return nums[0]
    #checking whether nums[0] or nums[n-1] is the single element
    if nums[0]!=nums[1]:
        return nums[0] 
    if nums[n-1]!=nums[n-2]:
        return nums[n-1]
    low=1
    high=n-2
    #checking for 1->n-2
    while low<=high:
        mid=(low+(high-low)//2)

        if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
            return nums[mid]
        #standing in the right half ->eliminate right acc to combined conditions
        if (mid%2==0 and nums[mid-1]==nums[mid]) or (mid%2==1 and nums[mid]==nums[mid+1]) :
            high=mid-1
        #standing in left half->eliminate left since ans in right
        else:
            low=mid+1
    return -1

print(op2(nums))

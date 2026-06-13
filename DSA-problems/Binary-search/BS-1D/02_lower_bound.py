'''Given a sorted array of nums and an integer x, write a program to find the lower bound of x.

The lower bound algorithm finds the first and smallest index in a sorted array where the value at that index is greater than or equal to a given key i.e. x.

If no such index is found, return the size of the array.'''
nums= [3,5,8,12,13,15,19]
x = 9
#lower bound mean: "Where should I insert x so the array remains sorted?"
def brute(nums,x):
    lb=len(nums)
    for i in range(len(nums)):
        if nums[i]>=x:
            lb=i
            break
    return lb


#tc=- o(log n), sc-o(n)
def optimal(nums,x):
    low=0
    high=len(nums)-1
    lb=len(nums)
    while low<=high:
        mid=(low+(high-low)//2)
        #once found we eliminate the right half caz we want a num >= x
        # and search in left half only(else cond)
        if nums[mid]>=x:
            lb=mid
            high=mid-1
        #if smaller numbers we keep searching for larger ones
        else:
            low=mid+1
    return lb
print(optimal(nums,x))
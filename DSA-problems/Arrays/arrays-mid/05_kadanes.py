'''Given an integer array nums, find the subarray with the largest sum, and return its sum.
'''
nums= [-2, -3, -7, -2, -10, -4]
#----Brute force----O(n^3)---O(1)
def maxs(nums):
    max_sum=float('-inf')
    for i, inum in enumerate(nums):
        for j in range(i, len(nums)):
            sum=0
            for k in range(i,j+1):
                sum+=nums[k]
            if sum>max_sum:
                max_sum=sum
    return max_sum
# print(maxs(nums))


#Better soln---O(n^2)--O(1)--
def maxxs(nums):
    max_sum=float('-inf')
    for i in range(0,len(nums)):
        sum=0
        for j in range(i,len(nums)):
            sum+=nums[j]
            if sum>max_sum:
                max_sum=sum
    return max_sum
# print(maxxs(nums))
        
    
#--------kadane's algorithm- MOST OPTIMAL--O(n)--O(1)----
nums=[-2,1,-3,4,-1,2,1,-5,4]
def maxss(nums):
    max_sum=float('-inf')
    i=0
    sum=0
    while i<len(nums):
        sum+=nums[i]
        if sum<0:
            sum=0
            i+=1
            continue
        if sum>max_sum:
            max_sum=sum
        i+=1
    return max_sum
# print(maxss(nums))
        
#including negs in sum returned
# NOTE: here instead of checking and discarding when sum < 0: , we are 
# comparing sum to its RELATIVE element(sum<nums[i]) so that even if only returned sum possiblity is negative
# negative sum is also returned 
def maxsub(nums):
    sum=nums[0]
    max_sum=nums[0]
    for i in range(1,len(nums)):
        sum+=nums[i]   #Add next el
        if nums[i]>sum: #compare if sum is greater than current el added
            sum=nums[i] #if it is then DROP sum and assign nums[i] as sum (DROP AND RESTART)
                        # if not then continue with the sum (KEEP ADDING)
        if sum>max_sum:#compare w max_sum ans assign new max
            max_sum=sum
    return max_sum
# print(maxsub(nums))

# -------------kadane's with returning sub array too
# A subarray is a contiguous non-empty sequence of elements within an array.
def maxsubb(nums):
    if not nums:
        return 0, -1, -1
    sum=nums[0]
    max_sum=nums[0]
    start=0
    fstart=0
    fend=0
    for i in range(1,len(nums)):
        sum+=nums[i]
        # print(start)
        if nums[i]>sum:
            sum=nums[i]
            start=i
        if sum>max_sum:
            max_sum=sum
            fstart=start
            fend=i
    return max_sum, fstart, fend
print(maxsubb(nums))

p=[-2,1,-3,4,-1,2,1,-5,4]
def prac(nums):
    sum=0
    max_sum=nums[0]
    for i in range(1,len(nums)):
        sum+=nums[i]
        if nums[i]>sum:
            sum=nums[i]
        if sum>max_sum:
            max_sum=sum
    return max_sum
print(prac(p))
# all subarrays
def print_subarr(nums):
    lst=[]
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            s=[]
            for k in range(i,j+1):
                
                s.append(nums[k])
            lst.append(s)
    print(lst)
print_subarr(nums)
                
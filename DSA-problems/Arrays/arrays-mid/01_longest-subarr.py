# Given an array nums of size n and an integer k, find the length of the longest sub-array that sums to k. 
# If no such sub-array exists, return 0.
import array as a

nums=a.array('i',[10,2,5,3,2,1,0,1,6,0,0,0,0])
target=12
#( FAILED )Longest sub-array that contains sum of tatrget 
# def longsub(nums,target):
#     count=1
#     maxc=0
#     lasti=0
#     lastj=0
#     for i in range(0,len(nums)):
#         sum=nums[i]
#         count=1
#         for j in range(i+1,len(nums)):
#             if sum<target:
#                 sum+=nums[j]
#                 count+=1
#                 maxc=max(count,maxc)
#             elif sum==target:
#                 lasti=i
#                 lastj=j
#             else:
#                 if count>maxc:
#                     lasti=i
#                     lastj=j
#                 break

#     return lasti,lastj


# print(longsub(nums,target))
#nums=a.array('i',[10,2,5,3,2,1,0,1,6,0,0,0,0])

#---------------------using hashmap---------O(n) o(n)---------------
#key=sum, value=index
#storing the earliest index - is fo maximizing the array length,
# if same length found at 3,6,8 indices then choosing 3 till the 9 gives longest subarray
#{0:-1} for calculating length correctly if subarray length calculated from 0 index,
# (2-0)gives 2 but lenth is three so at 0 sum length=-1, giving (2-(-1))=3 length
# Slice rule: Python slices go left → right
def longest_subarray_sum(nums, target):
    prefix_sum_map = {0:-1}
    prefix_sum = 0
    max_len = 0

    for i, num in enumerate(nums):
        prefix_sum += num

        # Case 1: from start to current index
        if prefix_sum == target:
            max_len = max(max_len, i + 1)

        # Case 2: target found between earlier index and now
        if (prefix_sum - target) in prefix_sum_map:
            length = i - prefix_sum_map[prefix_sum - target]
            max_len = max(max_len, length)

        # Store earliest index for this prefix_sum
        if prefix_sum not in prefix_sum_map:
            prefix_sum_map[prefix_sum] = i

    return max_len

def longest_sub12(nums,target):
    hashmap={0:-1}
    prefix_sum=0
    maxl=0
    start=end=-1
    # start and end are never assigned
    # They don’t exist
    for i in range(len(nums)):
        prefix_sum+=nums[i]
        if (prefix_sum-target) in hashmap:
            length=i-hashmap[prefix_sum-target]
            if length>maxl:
                maxl=length
                start=hashmap[prefix_sum-target]+1
                end=i
        if prefix_sum not in hashmap:
            hashmap[prefix_sum]=i
#--------------------longest_sub_positive---O(n^2)-------


def longsub(nums,target):
    count=1
    maxc=0
    for i in range(len(nums)):
        sum=nums[i]
        count=1
        for j in range(i+1,len(nums)):
            if sum<target:
                sum+=nums[j]
                count+=1
                
            if sum==target:
                maxc=max(count,maxc)
            if sum>target:
                break
    return maxc

# print(longsub(nums,target))

#OPTIMAL SLIDING WINDOW--O(n) only and no space
def slidingSub(nums,target):
    start=0
    sum=0
    maxc=0
    for end in range(len(nums)):
        sum+=nums[end]

        while sum>target:
            sum-=nums[start]
            start+=1
        if sum==target:
            maxc=max(maxc,end-start+1)
    return max
#-----------longest_sub_negatives---O(n^2)--------
nums1 = [3,0]
target1 = 3

def longsubneg(nums,target):
    count=1
    maxc=0
    for i in range(len(nums)):
        sum=nums[i]
        count=1
        # single-element case fails as j loop never runs- so first check single element
        if sum == target:
            maxc = max(maxc, count)
        for j in range(i+1,len(nums)):
            # don't put the condition as it doesn't evaluate for above example
            # returns 1 even if 2 as it doesn't get into the condition for adding and is unnecessary to keep
            # if sum<target or sum>target:#or if sum != target:
            sum+=nums[j]
            count+=1
            print(sum)
            if sum==target:
                maxc=max(maxc,count)
    return maxc

print(longsubneg(nums1,target1))

# practice
def prac_sliding(nums):
    start=0
    sum=0
    max_len=0
    for end in range(len(nums)):
        sum+=nums[end]
        
        while sum<target and start<=end:
            sum-=nums[start]
            start+=1
        if sum==target:
            max_len=max(max_len,end-start+1)
    return max_len   
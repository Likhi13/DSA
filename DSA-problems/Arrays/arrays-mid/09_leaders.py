'''
Given an integer array nums, return a list of all the leaders in the array.
A leader in an array is an element whose value is strictly greater than all elements
to its right in the given array.
The rightmost element is always a leader. 
The elements in the leader array must appear in the order they appear in the nums array.
'''

#Brute Force
def leader(nums):
    arr=[]
    for i in range(len(nums)):
        max=float("-inf")
        count=0
        for j in range(i+1,len(nums)):
            if nums[i]>nums[j]:
                count+=1
            else:
                break
        if count==(len(nums)-i-1):
            arr.append(nums[i])
    return arr
nums=[-3,4,5,1,-4,-5]
# print(leader(nums))

# def leader_op(nums):
#     arr=[]
#     arr.append(nums[len(nums)-1])
#     i=len(nums)-1
#     j=i-1
#     while j>=0:
#         if nums[j]>nums[i]:
#             arr.append(nums[j])
#         j-=1
#         leader=False
#         i=len(nums)-1
#         while i>j:
#             if nums[j]>nums[i]:
#                 leader=True
#             else:
#                 leader=False
#                 break
#             i-=1
#         if leader==True:
#             arr.append(nums[j])
#     l=0
#     r=len(arr)-1
#     while l<r:
#         arr[l],arr[r]=arr[r],arr[l]
#         l+=1
#         r-=1
#     return arr

# print(leader_op(nums))
            
def leader_op(nums):
    leaders=[]
    max_num=nums[len(nums)-1]
    leaders.append(max_num)
    for i in range(len(nums)-1,0,-1):
        if nums[i]>max_num:
            leaders.append(nums[i])
            max_num=nums[i]
    l=0
    r=len(leaders)-1
    while l<r:
        leaders[l],leaders[r]=leaders[r],leaders[l]
        l+=1
        r-=1
    
        
    return leaders

print(leader_op(nums))

        
        
        
          


            
        
        
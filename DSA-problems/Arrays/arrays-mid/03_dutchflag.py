'''Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.'''
# from collections import deque
# ----------------------------Sort an array of 0's 1's and 2's-in place
nums= [0,0,0,0,0,2,2,2,2,2,1,1,1,1,1]
def sorting(nums):
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            if nums[i]>nums[j]:
                nums[i],nums[j]=nums[j],nums[i]
    return nums

# print(sorting(nums)) 

# better soln--O(2N)--
def sorts(nums):
    c1=c2=c3=0
    for i in range(len(nums)):
        if nums[i]==0:
            c1+=1
        elif nums[i]==1:
            c2+=1
        else:
            c3+=1
    print(c1,c2,c3)
    for i in range(0,c1):
        nums[i]=0
    for i in range(c1,c1+c2):
        nums[i]=1
    for i in range(c1+c2,len(nums)):
        nums[i]=2
    return nums
# print(sorts(nums))

#--optimal-dutch flag soln--
def sorts1(nums):
    low=mid=0
    high=len(nums)-1
    while mid<=high:
        if nums[mid]==0:
            nums[low],nums[mid]=nums[mid],nums[low]
            mid+=1
            low+=1
        elif nums[mid]==1:
            mid+=1
        else:
            nums[mid],nums[high]=nums[high],nums[mid]
            high-=1
    return nums
print(sorts1(nums))
        
        
p=[2, 0, 1]
     
def prac1(nums):
    mid=0
    low=0
    high=len(nums)-1
    while mid<=high:
        if nums[mid]==0:
            nums[low],nums[mid]=nums[mid],nums[low]
            low+=1
            mid+=1
        elif nums[mid]==1:
            mid+=1
        else:
            nums[high],nums[mid]=nums[mid],nums[high]
            high-=1
    return nums
print(prac1(p))
    





#fAILED APPROACH HASHMAP+DEQUE


# def sort012(nums):
#     # {0:[1,4],1:[0,3],2:[2]}
#     #hashmap
#     hashmap={}
#     for i,num in enumerate(nums):
#         if num not in hashmap:
#             hashmap[num]=deque([])
#         hashmap[num].append(i)
#     print(hashmap)
#     for k in [0, 1, 2]:
#         if k not in hashmap:
#             hashmap[k] = deque([])
#     while True:
#         swapped=False
        
#         if hashmap[0] and hashmap[1] and hashmap[0][0]>hashmap[1][0]:
#             i0,i1=hashmap[0][0],hashmap[1][0]
#             nums[i0],nums[i1]=nums[i1],nums[i0]
#             hashmap[0].popleft()
#             hashmap[1].popleft()
#             hashmap[0].append(i1)
#             hashmap[1].appendleft(i0)
#             swapped=True
#         if hashmap[0] and hashmap[2] and hashmap[0][0]>hashmap[2][0]:
#             i0, i2 = hashmap[0][0], hashmap[2][0]
#             nums[i0], nums[i2] = nums[i2], nums[i0]
#             hashmap[0].popleft()
#             hashmap[2].popleft()
#             hashmap[0].append(i2)
#             hashmap[2].appendleft(i0)
#             swapped = True
#         if hashmap[1] and hashmap[2] and hashmap[1][0] > hashmap[2][0]:
#             i1, i2 = hashmap[1][0], hashmap[2][0]
#             nums[i1], nums[i2] = nums[i2], nums[i1]
#             hashmap[1].popleft()
#             hashmap[2].popleft()
#             hashmap[1].append(i2)
#             hashmap[2].appendleft(i1)
#             swapped = True
#         if not swapped:
#             break
#     return nums

    
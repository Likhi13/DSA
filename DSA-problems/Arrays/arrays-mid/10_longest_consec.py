'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 '''
nums= [100,1,1,1,1,2,2,1,4,200,1,3,2,2]

def brute2(nums):
    # selecting the correct sequence start
    unique=set(nums)
    sort=sorted(unique)

    max_len=1
    print(sort)
    for i in range(len(sort)): 
        length=1
        for k in range(1,len(sort)):
            if sort[i]+k in unique:
                length+=1
            else:
                break
            if length>max_len:
                max_len=length
    return max_len
# print(brute2(nums))

def better(nums):
    if len(nums)==0:
        return 0
    sort=sorted(nums)
    longest=1
    last_small=float('inf')
    curr_count=0
    for i in range(len(sort)):
        if sort[i]==last_small+1:
            curr_count+=1
            last_small=sort[i]
        elif sort[i]!=last_small:
            last_small=sort[i]
            curr_count=1
        longest=max(curr_count,longest)
    return longest
print(better(nums))
#TC=O(N)+O(N)+O(N)=O(3N)--SC=O(N)
def optimal1(nums):
    unique=set(nums)
    max_len=0
    for num in unique:#O(n)
        if num-1 not in unique:
            length=1
            current=num
            while current+1 in unique:#O(N)
                current+=1
                length+=1
            max_len=max(max_len,length)
    return max_len  
                
# print(optimal1(nums))

#FAILED BRUTE 
# def brute1(nums):
#     hashmap={}
#     for i in range(len(nums)):
#         len_i=1
#         for k in range(1,len(nums)+1):
#             if nums[i]+k in nums:
#                 len_i+=1
#         print(len_i)       
#         for key,value in enumerate(nums):
#             if value not in hashmap: 
#                 hashmap[value]=len_i
#     max_len=0
#     print(hashmap)
#     for key in hashmap:
#         if hashmap[key]>max_len:
#             max_len=hashmap[key]
#     return max_len
# print(brute1(nums))




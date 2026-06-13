'''You are given an integer array arr of size n which contains both positive and negative integers. Your task is to find the length of the longest contiguous subarray with sum equal to 0.



Return the length of such a subarray. If no such subarray exists, return 0.'''
nums=  [0, 1, 7, 10, 23]

# TC-O(n^3)--sc=o(1)
def brute(nums):
    arr=[]
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            sub=[]
            for k in range(i,j+1):
                sub.append(nums[k])
            arr.append(sub)
    max_length=0
    length=0
    for i in range(len(arr)):
        sum=0
        length=0
        for j in range(len(arr[i])):
            sum+=arr[i][j]
            length+=1
            if sum==0:
                max_length=max(max_length,length)
    return max_length
    

# print(brute(nums))
#TC= O(N^2)--SC=0(1)  
def better(nums):
    length=0
    max_length=0
    for i in range(len(nums)):
        sum=0
        for j in range(i,len(nums)):
            sum+=nums[j]
            if sum==0:
                length=j-i+1
                max_length=max(max_length,length)
    return max_length
print(better(nums))
#TC=O(N)--SC=O(N)
def optimal(nums):
    hashmap={0:-1}
    prefix_sum=0
    max_length=0
    
    for i in range(len(nums)):
        prefix_sum+=nums[i]
        
        if prefix_sum-0 in hashmap:
            length=i-hashmap[prefix_sum-0]
            max_length=max(length,max_length)
         
        if prefix_sum not in hashmap:
            hashmap[prefix_sum]=i
    return max_length
print(optimal(nums))
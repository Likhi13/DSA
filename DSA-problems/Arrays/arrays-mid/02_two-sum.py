'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any orde'''
#-------------------TWO_SUM-------------
nums = [3,2,1,3]
target = 6

def two_sum(nums,target):
    hashmap={}
    for i,num in enumerate(nums):
        hashmap[num]=i
    print(hashmap)
    for i,num in enumerate(nums):
        # print(num)
        
        if target-num in hashmap and i!=hashmap[target-num]:#not same index
            return i,hashmap[target-num]
    return None

# print(two_sum(nums,target))
nums1 = [3,2,4,3]
target1 = 6
def two_summ(nums,target):
    for i in range(len(nums)):
        j=0
        while j<=(len(nums)-1):
            if j!=i:
                sum=nums[i]+nums[j]
                if sum==target:
                    return i,j
            j+=1
# print(two_summ(nums1,target1))/

def two_sum2(nums,target):
    hashmap={}
    for key,value in enumerate(nums):
        hashmap[value]=key
    for key,value in enumerate(nums):
        if (target-value) in hashmap and key!=hashmap[target-value]:
            return key,hashmap[target-value]

print(two_sum2(nums1,target1)) 

nums=[2, 3, 5, -2, 7, -4]
# def kadane(nums):
#     hashmap={0:-1}
#     prefix_sum=None
#     max=prefix_sum
#     for key,value in enumerate(nums):
#         if  prefix_sum==None:
#             prefix_sum=value
#         prefix_sum+=value
#         if prefix_sum
#         if prefix_sum not in hashmap:
#             hashmap[prefix_sum]=value 
def brutef(nums):
    max_val=0
    for i in range(len(nums)):
        sum=0
        sum=max_val
        for j in range(i,len(nums)):
            sum+=nums[j]
            if sum>max_val:
                max_val=sum
                left=i
                right=j
    flist=[]
    for i in range(left,right+1):
        flist.append(nums[i])
    return flist  

# practice
prac=[2, 3, 5, -2, 7, -4]
t=8
def practice1(nums,target):
    hashmap={}
    for key,value in enumerate(nums):
        if value not in hashmap:
            hashmap[value]=key
    print(hashmap)
    for key,value in enumerate(nums):
        if target-value in hashmap and key!=hashmap[target-value]:
            return (key,hashmap[target-value])
    
        
print(practice1(prac,t))
import array as a

nums=a.array('i', [1,2,3,4,6,1,2,3,4,5])


#------------------------Find the number that appears once, and other numbers twice-----o(n)----#
def uniquein2(nums):
    unique=0
    for i in range(len(nums)):
        unique^=nums[i]
    return unique

def uniquein2_0(nums):
    numss=sorted(nums)
    # print(numss)
    n=0
    while n<len(numss):
        if numss[n]==numss[n+1]:
            n=n+2
        else:
            return numss[n]
# print(uniquein2(nums))
nums1=[2,3,3,4,6,8,6,2,8,9,9,3,3,7,10,7,10,-1,-1]
# print(uniquein2_0(nums1))

def uniquein2_1(nums):
    hashmap={}
    i=0

    while i<len(nums):
        if nums[i] not in hashmap:
            hashmap[nums[i]]=[]
            hashmap[nums[i]].append(i)
        else:
            hashmap[nums[i]].append(i)
        i+=1
    for key,value in hashmap.items():
        if len(value)==1:
            return key

# print(uniquein2_1(nums1))

# hash={}
# hash[nums1[0]]=[]
# hash[nums1[0]].append(1)
# hash[nums1[0]].append(3)
# print(hash)

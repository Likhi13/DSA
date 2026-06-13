'''Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
'''

nums=[1,2]
def brute(nums):
    majority=len(nums)//3
    print(majority)
    maj=[]
    hashmap={}
    for i in range(len(nums)):
        if nums[i] not in hashmap:
            hashmap[nums[i]]=0

        hashmap[nums[i]]+=1
    for key in hashmap:
        if hashmap[key]>majority:
            maj.append(key)
    
    return maj
print(brute(nums))

def optimal(nums):
    n=len(nums)
    count1=0
    count2=0
    maj_1=None
    maj_2=None
    ans=[]
    
    for i in range(len(nums)):
        if nums[i]==maj_1:
            count1+=1
        elif nums[i]==maj_2 and nums[i]!=maj_1:
            count2+=1
        elif count1==0:
            maj_1=nums[i]
            count1=1
        elif count2==0 and nums[i]!=maj_1:
            maj_2=nums[i]
            count2=1
        elif nums[i]!=maj_1 and nums[i]!=maj_2:
            count1-=1
            count2-=1
            
    c1=0
    c2=0
    for i in range(len(nums)):
        if maj_1==nums[i]:
            c1+=1
        if maj_2 !=maj_1 and maj_2==nums[i]:
            c2+=1
    if c1>n//3:
        ans.append(maj_1)
    if c2>n//3:
        ans.append(maj_2)
    return ans
print(optimal(nums))
        
            
        
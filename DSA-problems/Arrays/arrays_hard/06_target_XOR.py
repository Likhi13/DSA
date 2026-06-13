'''Given an array of integers nums and an integer k,
return the total number of subarrays whose XOR equals to k.
'''
nums = [4, 2, 2, 6, 4]
k = 6
# TC=O(N^2), SC=O(1)
def brute(nums,target):
    arr=[]
    for i in range(len(nums)):
        sub=[]
        xor=0
        for j in range(i,len(nums)):
            xor^=nums[j]
            sub.append(nums[j])
            if xor==target:
                arr.append(sub.copy())
    return arr
    
print(brute(nums,k))

# worst TC=O(N^3) ELSE O(N), SC=O(N)-- BUT OPTIMAL CAZ RETURNING SUB ARRAYS CAN'T BE OPTIMIZEED, COUNTING CAN BE
def optimal(nums,target):
    hashmap={0:[-1]}
    arr=[]
    prefix_xor=0
    for i in range(len(nums)):
        prefix_xor^=nums[i]
         
        if prefix_xor^target in hashmap:
           
            k=0
            while k < len(hashmap[prefix_xor^target]):
                sub=[]
                start=hashmap[prefix_xor^target][k]
                end=i
                for j in range(start+1,end+1):
                    sub.append(nums[j])
                arr.append(sub)
                k+=1
            
        if prefix_xor not in hashmap:
            hashmap[prefix_xor]=[i]
        else:
            hashmap[prefix_xor].append(i)
    print(hashmap)
    return arr
print(optimal(nums,k))
    
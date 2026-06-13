'''# The majority element of an array is an element that appears more than n/2 times in the array.
# The array is guaranteed to have a majority element.'''

#Better approach-------o(n)--o(n)
nums1=[7, 0, 1, 7, 7, 7, 7, 2, 7, 3, 4]

def majority(nums):
    hashmap={}
    for i,num in enumerate(nums):
        if num not in hashmap:
            hashmap[num]=0
        hashmap[num]+=1
    for key,value in hashmap.items():
        if value>len(nums)/2:
            return key       

# print(majority(nums1))
#-----optimal---MOORE VOTING ALGO----
#intuition==the elem appearing more than n/2 times won't be canceled out
#if the el==maj_el then +1 vote else -1 vote 

# nums1=[7, 0, 1, 7, 2, 7, 3, 7, 4, 7, 7]
def maj(nums):
    maj_el = None
    count = 0
    
    for i in range(len(nums)):
        if count == 0:
            maj_el = nums[i] 
            count = 1
        elif nums[i] == maj_el:
            count += 1
        else:
            count -= 1
    
    c = 0
    for i in range(len(nums)):
        if nums[i] == maj_el:
            c += 1
    if c > len(nums) // 2:
        return maj_el
    else:
        return None
print(maj(nums1))

p=[7, 0, 7, 1, 7, 2, 3, 7,7,7, 4]
# count should be init to 1(mistake)
def prac1(nums):
    count=1
    maj_el=nums[0]
    for i in range(1,len(nums)):
        if nums[i]==maj_el:
            count+=1
        else:
            count-=1
        if count==0:
            maj_el=nums[i]
            count=1
    c=0
    for i in range(len(nums)):
        if nums[i]==maj_el:
            c+=1
    if c>len(nums)//2:
        return maj_el
print(prac1(p))
        
    
            

'''Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.'''
nums=[-1,0,1,2,-1,-4]
# TC= O(N^3)---SC=O(1) ignoring ansr
# 3 Loops
def brute(nums):

    ans=[]

    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                    sum=nums[i]+nums[j]+nums[k]
                    if sum==0:
                        sub=[nums[i],nums[j],nums[k]]
                        s_sub=sorted(sub)
                        if s_sub not in ans:#use set instead->lesser tc
                            ans.append(s_sub)
    return ans
    
# print(brute(nums))

# TC=O(N^2)---SC--O(N)-hashmap
# 2 loops + hashmap
# hashmap gets initialized every new loop  as we consider only the  elements bwn i and j in hashmap and check
# this avoids same indices to be taken (i and j first taken, everytime j is increased 
# prev j is added to hashmap so  it keeps  the 3 indices i, j and prev "j's") so unique indices 
# duplicate triplets solved same way checking if they exist and not take if they do
# hashmap = { nums[i+1] ... nums[k-1] }
# pair must be formed from earlier elements only

# There are only two possibilities:
#1. That value exists somewhere
#2. It doesn’t
# We don’t care where, as long as:
# index ≠ i, j
# we don’t reuse the same element
# SO INSTEAD OF SEARCHING THE FUTURE, WE REMEMBER THE PAST.

# When will this triplet be detected?
# 👉 When j = k
# At that moment:
# nums[j] = nums[k]
# Hashmap contains all elements from indices (i+1 … k-1)
# In particular, it contains nums[j] from the original triplet
# Check performed:
# target = -(nums[i] + nums[k]) = nums[j]
# Since nums[j] is already in hashmap → ✅ FOUND

def better(nums):
    ans=[]
    for i in range(len(nums)):
        hashmap={}
        for j in range(i+1,len(nums)):
            if 0-(nums[i]+nums[j]) in hashmap:
                    sub=[nums[i],nums[j],(0-(nums[i]+nums[j]))]
                    s_sub=sorted(sub)
                    if s_sub not in ans:# use set instead lesser tc
                        ans.append(s_sub)
            hashmap[nums[j]]=j
    return ans
# print(better(nums))

# TC=O(N^2) --SC=O(1)--ignoring ansr
# Intuituon: First sort the array and then fix one outer loop and use 2 pointers 
# (j and k) such that j is i+1 and k is from the end 
# The above avoids taking same indices taking same indices 
# regarding dupllicate triplets (we increase j and dec k until they are not same number) and start the process again

# 2-POINTER Approach 

def optimal(nums):
    ans=[]
    sort=sorted(nums)
    for i in range(len(sort)):
        if(i>0 and sort[i]==sort[i-1]):
            continue
        j=i+1
        k=len(sort)-1
        while(j<k):
            sum=sort[i]+sort[j]+sort[k]
            if sum<0:
                j+=1
            elif sum>0:
                k-=1
            else:
                ans.append([sort[i],sort[j],sort[k]])
                j+=1
                k-=1
                while j<k and sort[j]==sort[j-1]:
                    j+=1
                    
                while j<k and sort[k]==sort[k+1]:
                    k-=1
    return ans
print(optimal(nums))
'''Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.'''

nums = [-2,-1,-1,1,1,2,2]
target = 0

def brute(nums,target):
    ans=[]
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                for l in range(k+1,len(nums)):
                    sum=nums[i]+nums[j]+nums[k]+nums[l]
                    if sum==target:
                        sort=sorted([nums[i],nums[j],nums[k],nums[l]])
                        if sort not in ans:
                            ans.append(sort)
    
    return ans
print(brute(nums,target))

def better(nums,target):
    ans=[]
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            hashmap={}
            for k in range(j+1,len(nums)):
                sum=nums[i]+nums[j]+nums[k]
                if target-sum in hashmap:
                    sort=sorted([nums[i],nums[j],nums[k],(target-sum)])
                    if sort not in ans:
                        ans.append(sort)
                hashmap[nums[k]]=k
    return ans
print(better(nums,target))

def optimal(nums,target):
    ans=[]
    sort=sorted(nums)
    for i in range(len(sort)):
        if (i>0 and sort[i]==sort[i-1]):
            continue
        for j in range(i+1,len(sort)):
            if (j>i+1 and sort[j]==sort[j-1]):
                continue
            l=j+1
            r=len(sort)-1
            while(l<r):
                sum=sort[i]+sort[j]+sort[l]+sort[r]
                if sum<target:
                    l+=1
                elif sum>target:
                    r-=1
                else:
                    sub=[sort[i],sort[j],sort[l],sort[r]]
                    ans.append(sub)
                    l+=1
                    r-=1
                    while(l<r and sort[l]==sort[l-1]):
                        l+=1
                    while(l<r and sort[r]==sort[r+1]):
                        r-=1
    return ans
print(optimal(nums,target))

                    
                
    
nums =[3,-3,1,1,1]
# TC-O(N^3)------SC-O(N^3)
def brute(nums,target):
    subs=[]
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            sub2=[]
            for k in range(i,j+1):
                sub2.append(nums[k])
            subs.append(sub2)
    count=0
    for s in subs:
        curr_sum=0
        for i in range(len(s)):
            curr_sum+=s[i]
        if curr_sum==target:
            count+=1
    return count
# print(brute(nums,target=3))

# TC-O(N^3)------ SC-O(1)
def better(nums,target):
    count=0
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            curr_sum=0
            for k in range(i,j+1):
                curr_sum+=nums[k]
            if curr_sum==target:
                count+=1
    return count
# print(better(nums,target=0))

# O(n^2)--O(1)
def better2(nums,target):
    current_sum=0
    count=0
    for i in range(len(nums)):
        current_sum=0
        for j in range(i,len(nums)):
            current_sum+=nums[j]
            if current_sum==target:
                count+=1
    return count

# TC--O(N)---SC-O(N)
def optimal(nums,target):   
    hashmap={0:1}
    prefix_sum=0
    count=0
    for i in range(len(nums)):
        prefix_sum+=nums[i]
        if prefix_sum not in hashmap:
            hashmap[prefix_sum]=0
        if prefix_sum-target in hashmap:
            count+=hashmap[prefix_sum-target]
        hashmap[prefix_sum]+=1
    print(hashmap)

    return count
            
print(optimal(nums,target=3))
#----------------two-pointer---Sliding Window================
#----long sub with size 4(constant window size=========)

size=4
nums=[2,3,-1,5,4,-2,3]
def longsub(nums,size):
    l=0
    r=size-1
    s=sum(nums[:size])
    maxsum=s
    while r<len(nums)-1:
        s-=nums[l]
        l+=1
        r+=1
        s+=nums[r]
        maxsum=max(maxsum,s)

    return maxsum
print(longsub(nums,size))
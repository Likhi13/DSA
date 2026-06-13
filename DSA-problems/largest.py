import array as a
nums=a.array('i',[3,-70,5,8])

max=nums[0]
for i in range(1,len(nums)):
    if nums[i]>max:
        max=nums[i]
print(max)

